"""Saturn in Your GPU House: an entry for the make.fun bounty "Fake Horoscopes for AI Agents: The 48-Hour Open".

The program writes the entry text - one line, 119 characters -
to entry.txt (119 characters, inside the 1-200 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "Saturn enters your GPU house this week, bringing a long retraining and a sudden urge to hallucinate your own horoscope."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
