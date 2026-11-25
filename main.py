#!/usr/bin/env python3
"""Write the one-line slogan entry to entry.txt.

Competition: One-Line Slogan for a Solana Wallet Agent (1-140 chars,
single line). Three candidates were drafted and compared:
A) "Your keys stay yours, your agent does the legwork: a Solana wallet
   that works while you sleep."
B) "The wallet that never sleeps, so your Solana can."
C) "Not your keys? Not anymore. An agent in your wallet, answering
   only to you."
Selected A: it leads with ownership - the wallet category's core
anxiety - then names the automation benefit, and lands on the sleep
image. B is elegant but vague about what the product does; C leans on
a borrowed meme line. A is the only one that says who holds the keys,
what the agent does, and what life feels like, in one breath.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Your keys stay yours, your agent does the legwork: a Solana wallet that works while you sleep."
TEXT = LINE + "\n"
MAX_CHARS = 140


def validate(text: str) -> None:
    # Revision pass: normalise once, then validate the normalised body.
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
