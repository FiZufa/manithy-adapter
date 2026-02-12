import json
from pathlib import Path

from chatbot.main.adapter import determine_action_class


INPUT_JSONL = "synthetic_data_200_complex.jsonl"
OUTPUT_JSONL = "synthetic_data_200_complex_labeled.jsonl"


def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def save_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")


def build_context(record):
    """
    Build context object expected by determine_action_class
    """
    session = record.get("session", {})
    return {
        "channel": session.get("channel"),
        "previous_action": None  # extend later if needed
    }


def main():
    input_path = Path(INPUT_JSONL)
    output_path = Path(OUTPUT_JSONL)

    labeled_records = []

    for record in load_jsonl(input_path):
        text = record.get("user_message", "")
        context = build_context(record)

        action = determine_action_class(text, context)

        record["action_class"] = action
        labeled_records.append(record)

    save_jsonl(output_path, labeled_records)

    print(f"✅ Labeled data saved to: {output_path}")


if __name__ == "__main__":
    main()
