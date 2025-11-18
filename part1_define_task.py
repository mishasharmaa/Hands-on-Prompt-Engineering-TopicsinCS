# part1_define_task.py

EVAL_MESSAGES = [
    "The product is amazing!",
    "It stopped working after one day.",
    "It's okay, nothing special.",
    "I love the design but shipping was slow.",
    "Worst purchase ever."
]

TASK_DESCRIPTION = """
Task: Classify short customer messages as POSITIVE, NEGATIVE, or NEUTRAL.
Good output gives correct label + short explanation.
"""

QUALITY_CRITERIA = """
1. Correct sentiment label.
2. Short, clear explanation.
3. Format: <LABEL> - <reason>.
"""

def print_task():
    print("=== TASK DESCRIPTION ===")
    print(TASK_DESCRIPTION)
    print("\n=== QUALITY CRITERIA ===")
    print(QUALITY_CRITERIA)
    print("\n=== EVAL SET ===")
    for i, msg in enumerate(EVAL_MESSAGES, 1):
        print(f"{i}. {msg}")

if __name__ == "__main__":
    print_task()
