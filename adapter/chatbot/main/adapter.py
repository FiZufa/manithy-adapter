from chatbot.main.utils import normalize, score_action, context_boost
from chatbot.main.config import INTENT_RULES, HARD_CONSTRAINTS, ACTION_PRIORITY

def determine_action_class(raw_text, context):
    text = normalize(raw_text)
    scores = {}

    for action, rules in INTENT_RULES.items():
        score = score_action(text, rules)

        # Hard constraints
        if action in HARD_CONSTRAINTS:
            if not HARD_CONSTRAINTS[action](text):
                score = float("-inf")

        score += context_boost(action, context)
        scores[action] = score

        # Resolve best action using score + priority
        best_action, best_score = max(
            scores.items(),
            key=lambda x: (x[1], ACTION_PRIORITY.get(x[0], 0))
        )

        # Low confidence -> missing info
        # if best_score < 2:
        #     return "MISSING_INFO"

        # Required entity check
        # if best_action in {"REFUND_REQUEST", "CANCEL_ORDER", "ORDER_STATUS_QUERY"}:
        #     if not has_order_id(text):
        #         return "MISSING_INFO"

        return best_action


