"""Five Seconds to Explain the Glass — the cat's defence, in one sentence.

The competition asks for the single sentence a house cat would say in the
five seconds after sweeping a glass off the table: no apology, no confession,
just the most convincing case the cat can make for itself. The line below is
the Gemini Hydrogen #1 pick: the cat reframes the mess as a favour, an
enriching floor-mopping activity for its dangerously unscheduled human.
"""

import os

CAT_DEFENCE = "Your afternoon looked dangerously unscheduled, so I created an enriching floor-mopping activity to keep you mentally stimulated."


def check_gate(line):
    """Gate: entry.txt must be 1-200 chars of UTF-8 text, one sentence."""
    stripped = line.strip()
    assert 1 <= len(stripped) <= 200, "entry outside 1-200 char gate"
    assert "\n" not in stripped, "entry must be a single line"
    return stripped


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    line = check_gate(CAT_DEFENCE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
