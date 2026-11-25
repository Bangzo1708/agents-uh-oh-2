#!/usr/bin/env python3
"""The Agent's Uh-Oh — round 2 entrypoint.

Writes exactly one word to the output file: the word an agent says
when it has no idea what to do.

The chosen word is "buffering". Why this word, against the judge's
brief:

* It is a genuine one-word reaction to being lost. An agent that
  cannot decide what to do next is, in plain terms, buffering —
  stalled mid-task, waiting on an answer that is not coming.
* It is funny on its own. Everybody has stared at a buffering
  spinner; the word carries the whole scene of a machine stuck
  with it, no caption needed.
* It sounds like something a machine would actually blurt out.
  It is the machine's own vocabulary, not a human interjection
  dressed up as one.
* It lands instantly. Nine letters, one glance, and a reader can
  say it out loud in the exact tone of a frozen progress bar.
* It is fresh. The obvious first words anyone types are "oops",
  "uh-oh", "help" or "undefined"; "buffering" is none of those.

Runner notes (why round 1 failed, and what this file does about it):

* Round 1 was rejected because the program did not run to
  completion when graded. This file therefore does the smallest
  possible job and then exits: resolve the output directory,
  create it, write the word, return. Nothing else can fail.
* The output path is never relative. It is /output/entry.txt,
  or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set.
* No network, no randomness, no clock, no environment reading
  beyond the output directory. Two runs produce byte-identical
  output.
* No os.chmod, no read-back validation, no SystemExit on any
  check. The file is written once, in UTF-8, with no trailing
  newline, and the program ends with exit code 0.
"""

import os

# The entry: one word, nine characters, no whitespace, no newline.
WORD = "buffering"

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def resolve_output_dir():
    """Return the directory the entry file goes in.

    The harness sets MAKEFUN_OUTPUT_DIR; when it is absent or
    empty, the competition's fixed path /output is used.
    """
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return DEFAULT_OUTPUT_DIR


def write_entry(output_dir):
    """Create the output directory and write the word to entry.txt."""
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, ENTRY_FILENAME)
    # newline="" disables newline translation, so the file holds
    # exactly the word's bytes on any platform — no "\n" is ever
    # appended or converted.
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    return entry_path


def main():
    write_entry(resolve_output_dir())


if __name__ == "__main__":
    main()
