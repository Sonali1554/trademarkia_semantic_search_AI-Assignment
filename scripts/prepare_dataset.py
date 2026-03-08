import os
import tarfile
import re
import json
from tqdm import tqdm

RAW_DATA_PATH = "data/raw"
PROCESSED_PATH = "data/processed"
DATASET_FOLDER = "20_newsgroups"


def remove_headers(text):
    parts = text.split("\n\n", 1)
    if len(parts) > 1:
        return parts[1]
    return text


def remove_quotes(text):

    cleaned_lines = []

    for line in text.split("\n"):

        if not line.strip().startswith(">"):
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def remove_signature(text):

    return text.split("\n--")[0]


def clean_text(text):

    text = remove_headers(text)

    text = remove_quotes(text)

    text = remove_signature(text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def load_documents(dataset_path):

    documents = []

    categories = os.listdir(dataset_path)

    for category in categories:

        category_path = os.path.join(dataset_path, category)

        if not os.path.isdir(category_path):
            continue

        for file in os.listdir(category_path):

            file_path = os.path.join(category_path, file)

            with open(file_path, "r", errors="ignore") as f:

                text = f.read()

                text = clean_text(text)

                if len(text.split()) > 20:

                    documents.append(
                        {
                            "text": text,
                            "category": category
                        }
                    )

    return documents


def main():

    dataset_path = os.path.join(RAW_DATA_PATH, DATASET_FOLDER)

    docs = load_documents(dataset_path)

    os.makedirs(PROCESSED_PATH, exist_ok=True)

    output_file = os.path.join(PROCESSED_PATH, "documents.json")

    with open(output_file, "w") as f:

        json.dump(docs, f)

    print("Total cleaned documents:", len(docs))


if __name__ == "__main__":
    main()