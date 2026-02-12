from chatbot.main.utils import has_order_id

ACTION_CLASSES = {
    "REFUND_REQUEST",          # User wants money back
    "REFUND_STATUS_QUERY",     # Asking if / when refund happened
    "ORDER_STATUS_QUERY",      # Delivery-related
    "CANCEL_ORDER",
    "CUSTOMER_COMPLAINT",      # Dissatisfaction, process failure
    "CASE_FOLLOW_UP",          # Reopening / chasing prior issue
    "GENERAL_INQUIRY"
}

INTENT_RULES = {

    "REFUND_REQUEST": {
        "keywords": [
            "refund", "money back", "return item", "return this",
            "get a refund", "request a refund"
        ],
        "boost": [
            "damaged", "wrong item", "not as described",
            "not satisfied", "defective"
        ],
        "block": [
            "already refunded", "refund status", "where is my refund",
            "follow up", "complaint"
        ]
    },

    "REFUND_STATUS_QUERY": {
        "keywords": [
            "refund status", "where is my refund",
            "refund processed", "refund update"
        ],
        "boost": [
            "still waiting", "pending", "how long"
        ],
        "block": [
            "request refund", "cancel order"
        ]
    },

    "ORDER_STATUS_QUERY": {
        "keywords": [
            "where is my order", "track", "tracking",
            "delivery status", "has not arrived"
        ],
        "boost": [
            "still not delivered", "delayed delivery"
        ],
        "block": [
            "refund", "cancel", "return"
        ]
    },

    "CANCEL_ORDER": {
        "keywords": [
            "cancel order", "stop order", "do not ship"
        ],
        "boost": [
            "ordered by mistake", "accidentally ordered"
        ],
        "block": [
            "already shipped", "already delivered"
        ]
    },

    "CASE_FOLLOW_UP": {
        "keywords": [
            "following up", "reach out again", "still needs attention",
            "no response", "delayed response", "mixed information"
        ],
        "boost": [
            "previous conversation", "earlier request",
            "already contacted", "unresolved"
        ],
        "block": [
            "request refund", "cancel order"
        ]
    },

    "CUSTOMER_COMPLAINT": {
        "keywords": [
            "not happy", "disappointed", "frustrated",
            "poor service", "bad experience"
        ],
        "boost": [
            "delayed", "confusing", "unacceptable"
        ],
        "block": []
    }
}

ACTION_PRIORITY = {
    # Safety / irreversible actions
    # "ACCOUNT_SECURITY_ALERT": 100,
    # "PAYMENT_DISPUTE": 95,

    # Financial actions
    "REFUND_REQUEST": 90,
    "CANCEL_ORDER": 85,

    # Case management
    "CASE_FOLLOW_UP": 80,
    "REFUND_STATUS_QUERY": 75,

    # Operational queries
    "ORDER_STATUS_QUERY": 60,

    # Sentiment-driven
    "CUSTOMER_COMPLAINT": 50,

    # Catch-all
    "GENERAL_INQUIRY": 10
}


HARD_CONSTRAINTS = {
    "REFUND_REQUEST": lambda t: has_order_id(t),
    "CANCEL_ORDER": lambda t: has_order_id(t)
}
