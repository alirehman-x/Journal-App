import re
from pathlib import Path
from write_logs import logs_directory
def search():
    keyword = input("Enter the keyword you wanna search: ").lower()
    results = {}

    for entry_path in logs_directory.glob("*.txt"):
        try:
            content = entry_path.read_text(encoding="utf-8")
            sentences = re.split(r'(?<=[.!?])\s+', content)

            matching_sentences = []
            for sentence in sentences:
                if keyword in sentence.lower():
                    matching_sentences.append(sentence.strip())

            if matching_sentences:
                results[str(entry_path)] = matching_sentences

        except Exception as e:
            print(f"Could not read file {entry_path}: {e}")

    if results:
        for file_path, matching_sentences in results.items():
            filename = Path(file_path).name
            print(f"[File] {filename}")
            print(f"   Full Path: {file_path}")
            print(f"   Matches: {len(matching_sentences)}")
            for sentence in matching_sentences:
                print(f"   >> {sentence}")
            print("*********************************************************")
    else:
        print("No matches found.")
