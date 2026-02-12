import re

# Step 1: Normalize inputs
def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", text.lower())).strip()

# Step 2: Define lexical intent rules

# Step 3: Score each action
def score_action(text, rules):
    score = 0

    for kw in rules.get("keywords", []):
        if kw in text:
            score += 3

    for kw in rules.get("boost", []):
        if kw in text:
            score += 1

    for kw in rules.get("block", []):
        if kw in text:
            score -= 2

    return score

# Step 4: Extract hard entities
ORDER_ID_PATTERN = r"\b(ord[-_]?\d+)\b"

def has_order_id(text):
    return re.search(ORDER_ID_PATTERN, text) is not None

# Step 5: Context boost
def context_boost(action, context):
    boost = 0
    if action == "REFUND_REQUEST" and context.get("previous_action") == "ORDER_STATUS_QUERY":
        boost += 2
    if context.get("channel") == "voice":
        boost += 0.5
    return boost



