#!/usr/bin/env python3
"""The close-out hook: when a session stops, write its note into the task document.

Claude Code and Codex both run this when a turn or a session ends (see
.claude/settings.json and .codex/hooks.json). It reads the session's transcript,
takes what was asked first and what the agent said last, and keeps ONE dated line
per session under "## Session notes" in the task document the session worked on.
The line is rewritten in place as the session goes on, so a long session still
leaves one line.

It never calls a model, never blocks the agent and never fails the session: any
problem ends quietly with exit 0. Standard library only.

Usage (from a hook): python3 tools/close-out.py claude|codex   (hook JSON on stdin)
"""
import datetime
import json
import os
import re
import sys
from pathlib import Path

try:
    import fcntl  # file locking on macOS and Linux
except ImportError:  # Windows: no lock, the note is still written
    fcntl = None

ROOT = Path(__file__).resolve().parent.parent
TOOL = {"claude": "Claude Code", "codex": "Codex"}
HEADING = "## Session notes"


def texts(content):
    """The plain text inside a message's content (a string or a list of blocks)."""
    if isinstance(content, str):
        return [content]
    out = []
    for block in content if isinstance(content, list) else []:
        if isinstance(block, dict) and block.get("type") in ("text", "input_text", "output_text"):
            out.append(block.get("text") or "")
    return out


def messages(path):
    """(role, text, model) for every user and assistant message in a transcript."""
    found = []
    try:
        lines = Path(path).read_text(errors="replace").splitlines()
    except OSError:
        return found
    for line in lines:
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if not isinstance(row, dict):
            continue
        # Claude Code: {"type": "user"|"assistant", "message": {...}}
        # Codex: {"type": "response_item", "payload": {"type": "message", "role": ...}}
        msg = row.get("message") if isinstance(row.get("message"), dict) else row.get("payload")
        if not isinstance(msg, dict):
            continue
        if row.get("type") == "turn_context" and msg.get("model"):
            found.append(("model", "", msg["model"]))  # Codex names its model here
            continue
        role = msg.get("role") or row.get("type")
        if role not in ("user", "assistant"):
            continue
        for text in texts(msg.get("content")):
            text = text.strip()
            if text:
                found.append((role, text, msg.get("model") or row.get("model") or ""))
    return found


def one_line(text, limit):
    text = re.sub(r"\s+", " ", re.sub(r"[`*#>|]", "", text)).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def main():
    tool = sys.argv[1] if len(sys.argv) > 1 else "claude"
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        payload = {}
    transcript = payload.get("transcript_path") or ""
    if not transcript and tool == "codex" and payload.get("session_id"):
        # Codex keeps each session as ~/.codex/sessions/YYYY/MM/DD/rollout-<time>-<id>.jsonl
        home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
        hits = sorted(home.glob(f"sessions/*/*/*/rollout-*{payload['session_id']}.jsonl"))
        transcript = str(hits[-1]) if hits else ""
    log = messages(transcript)
    # skip what the tool injected itself: tagged blocks and Codex's copy of AGENTS.md
    asked = [t for r, t, _ in log if r == "user" and not t.startswith(("<", "# AGENTS.md instructions"))]
    said = [t for r, t, _ in log if r == "assistant"]
    last = (payload.get("last_assistant_message") or (said[-1] if said else "")).strip()
    if not asked or not last:
        return
    model = payload.get("model") or next((m for _, _, m in reversed(log) if m), "")

    tasks = sorted((ROOT / "tasks").glob("*.md"))
    # the task document named most recently in the session is the one it worked on;
    # with no name anywhere, a department with a single task document uses that one
    doc = None
    for _, text, _ in reversed(log):
        hits = [p for p in tasks if p.name in text]
        if hits:
            doc = max(hits, key=lambda p: text.rfind(p.name))
            break
    if doc is None and len(tasks) == 1:
        doc = tasks[0]
    if doc is None:
        return

    session = str(payload.get("session_id") or payload.get("thread_id") or "")[:8] or "nosession"
    who = TOOL.get(tool, tool) + (f" ({model})" if model else "")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    marker = f"<!-- session:{tool}-{session} -->"
    line = f'- {stamp} · {who} · asked: "{one_line(asked[0], 90)}" · did: {one_line(last, 220)} {marker}'

    with open(ROOT / "tasks" / ".close-out.lock", "w") as lock:
        if fcntl:
            fcntl.flock(lock, fcntl.LOCK_EX)
        body = doc.read_text()
        if marker in body:
            body = "\n".join(line if marker in old else old for old in body.split("\n"))
        elif HEADING in body:
            head, tail = body.split(HEADING, 1)
            nxt = re.search(r"\n## ", tail)
            section, rest = (tail[: nxt.start()], tail[nxt.start():]) if nxt else (tail, "")
            body = head + HEADING + section.rstrip("\n") + "\n" + line + "\n" + rest
        else:
            body = body.rstrip("\n") + f"\n\n{HEADING}\n\n{line}\n"
        doc.write_text(body)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    if len(sys.argv) > 1 and sys.argv[1] == "codex":
        print("{}")
