import os
from pdfminer.high_level import extract_text

# Get all PDF files in the current directory
files = [f for f in os.listdir() if f.lower().endswith(".pdf")]

for filename in files:
    try:
        print(f"Processing {filename}...")
        text = extract_text(filename)

        output_filename = f"{os.path.splitext(filename)[0]}_output.txt"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Text extracted and saved to {output_filename}")
    except Exception as e:
        print(f"Failed to process {filename}: {e}")
# This script extracts text from all PDF files in the current directory