# part2_zero_shot.py
import google.generativeai as genai
import os
from part1_define_task import EVAL_MESSAGES

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("models/gemini-2.0-flash")

ZERO_SHOT_PROMPT = """
You are a sentiment classifier.
Label each message as POSITIVE, NEGATIVE, or NEUTRAL.
Format your answer like this:
<LABEL> - <short reason>.
"""

def classify_zero_shot(message):
    response = model.generate_content(
        ZERO_SHOT_PROMPT + f"\nMessage: '{message}'"
    )
    return response.text

def run_zero_shot_eval():
    print("=== ZERO SHOT RESULTS ===")
    for msg in EVAL_MESSAGES:
        ans = classify_zero_shot(msg)
        print(f"\nInput: {msg}\nOutput: {ans}")

if __name__ == "__main__":
    run_zero_shot_eval()
