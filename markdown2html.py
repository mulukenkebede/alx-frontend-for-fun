import sys
import os
import markdown

if len(sys.argv) < 3:
    print("Usage: python markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

with open(input_file, "r") as f:
    markdown_text = f.read()

html_text = markdown.markdown(markdown_text)

with open(output_file, "w") as f:
    f.write(html_text)

sys.exit(0)
