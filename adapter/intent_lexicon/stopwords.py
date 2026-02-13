import os

MANUAL_STOPWORDS = [

    # Articles
    "a", "an", "the",

    # Pronouns
    "i", "me", "my", "mine", "myself",
    "we", "us", "our", "ours",
    "you", "your", "yours",
    "he", "she", "it", "they", "them", "their",

    # Common Verbs (non-informative)
    "am", "is", "are", "was", "were",
    "be", "been", "being",
    "do", "does", "did",
    "have", "has", "had",
    "would", "could", "should",
    "can", "may", "might",
    "will", "shall",

    # Connectors
    "and", "or", "but", "if", "because",
    "so", "although", "though",
    "while", "whereas",

    # Prepositions
    "in", "on", "at", "by", "for",
    "with", "about", "against",
    "between", "into", "through",
    "during", "before", "after",
    "above", "below", "to", "from",
    "up", "down", "out", "off",
    "over", "under",

    # Question words
    # "what", "which", "who", "whom",
    # "whose", "when", "where", "why", "how",

    # Politeness / filler
    "please", "kindly",
    "hi", "hello", "hey",
    "thanks", "thank", "thankyou",
    "regards", "dear",

    # Time fillers
    "just", "still", "already",
    "yet", "now", "today",

    # Conversational fillers
    "actually", "basically",
    "really", "very",
    "quite", "literally",
    "simply",

    # Common noise
    "regarding", "about",
    "somewhat", "somehow",
    "something", "anything",
    "everything", "nothing"
]

PROTECTED_WORDS = {"not", "no", "never"}


def _load_external_stopwords():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "EN-Stopwords.txt")

    external_stopwords = set()

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip().lower()
                if word:
                    external_stopwords.add(word)

    return external_stopwords

# Merge everything
STOPWORDS = (
    MANUAL_STOPWORDS
    | _load_external_stopwords()
) - PROTECTED_WORDS
