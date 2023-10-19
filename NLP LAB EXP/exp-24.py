import re

def recognize_dialog_acts(utterance):
    
    patterns = [
        (r'^(hello|hi|hey)$', 'GREETING'),
        (r'^(yes|no|maybe)$', 'ANSWER'),
        (r'^(what|who|where|when|why|how)', 'QUESTION'),
        (r'^[A-Z][a-zA-Z\s]*\?$', 'QUESTION'),
        (r'^[A-Z][a-zA-Z\s]*\!$', 'EXCLAMATION'),
        (r'^[A-Z][a-zA-Z\s]*\.$', 'STATEMENT'),
        (r'^[A-Z][a-zA-Z\s]*$', 'STATEMENT'),
    ]

    for pattern, dialog_act in patterns:
        if re.match(pattern, utterance, re.I):
            return dialog_act

    return 'UNKNOWN'


conversation = [
    "Hello, how are you?",
    "I'm good, thanks!",
    "What's your name?",
    "My name is ChatGPT.",
    "That's amazing!",
    "Can you help me with a question?",
]


for utterance in conversation:
    dialog_act = recognize_dialog_acts(utterance)
    print(f"Utterance: '{utterance}' - Dialog Act: {dialog_act}")
