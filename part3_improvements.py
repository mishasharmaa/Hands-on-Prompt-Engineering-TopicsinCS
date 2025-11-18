# part3_improvements.py
import google.generativeai as genai
import os
from part1_define_task import EVAL_MESSAGES

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("models/gemini-2.0-flash")

FEW_SHOT_PROMPT = """
You are a sentiment classifier.

Examples:
Message: "I love this so much!"
Answer: POSITIVE - expresses strong enjoyment

Message: "This is terrible."
Answer: NEGATIVE - describes a bad experience

Message: "It's fine, nothing special."
Answer: NEUTRAL - expresses average feelings

Now classify the new message:
Format: <LABEL> - <reason>
"""

COT_PROMPT = """
You are a sentiment classifier.
Think step-by-step about the message.
Then output final answer in:
<LABEL> - <short reason>
"""

SELF_CRIT_PROMPT = """
You are a sentiment classifier.
1. Think step-by-step.
2. Output <LABEL> - <reason>
3. Check and correct mistakes.
"""

def ask(prompt, message):
    response = model.generate_content(
        prompt + f"\nMessage: '{message}'"
    )
    return response.text

def run_all_improvements():
    print("\n=== FEW SHOT ===")
    for msg in EVAL_MESSAGES:
        print(msg)
        print(ask(FEW_SHOT_PROMPT, msg), "\n")

    print("\n=== CHAIN OF THOUGHT ===")
    for msg in EVAL_MESSAGES:
        print(msg)
        print(ask(COT_PROMPT, msg), "\n")

    print("\n=== SELF CRITIQUE ===")
    for msg in EVAL_MESSAGES:
        print(msg)
        print(ask(SELF_CRIT_PROMPT, msg), "\n")

if __name__ == "__main__":
    run_all_improvements()
