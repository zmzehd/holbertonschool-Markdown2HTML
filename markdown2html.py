#!/usr/bin/python3
"""Script that checks argument count and file existence for
converting Markdown to HTML.
Exits with error codes and messages if usage is incorrect or file is missing.
"""
import sys
import os

if __name__ == "__main__":
    # your existing code here

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", 
        file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)
