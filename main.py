"""make.fun entry: The Funniest Sick-Day Excuse (sick-day-A).

Writes one original sick-day excuse line to /output/entry.txt.
Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 200
characters, not only white space. The entry is a single line.
"""

import os

# The entry: one line, my own invention. A cracked tooth on a bagel is a
# half-believable reason to miss work; the dentist can only see me today,
# and the punch ("choosing chewing over capitalism") lands at the end.
ENTRY = (
    "My tooth cracked on a bagel this morning and the dentist can only "
    "see me today, so I'm choosing chewing over capitalism."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(text))
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    with open(path, encoding="utf-8") as f:
        text = f.read()
    print("Wrote %s (%d chars, %d line(s))" % (path, len(text), text.count("\n") + 1))
    print(text)


if __name__ == "__main__":
    main()
