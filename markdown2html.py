#!/usr/bin/python3
"""Script that converts Markdown headings to HTML."""
import sys
import os

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                line = line.strip()
                if line.startswith("#"):
                    count = 0
                    for char in line:
                        if char == "#":
                            count += 1
                        else:
                            break
                    # Heading must have space after #s
                    if count <= 6 and len(line) > count and line[count] == " ":
                        content = line[count + 1 :]
                        outfile.write(f"<h{count}>{content}</h{count}>\n")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
