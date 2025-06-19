questions = [
    {
        "question": "What is 2+2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Largest planet?",
        "options": ["Earth", "Jupiter", "Saturn", "Mars"],
        "answer": "Jupiter"
    },
    {
        "question": "2^3 equals?",
        "options": ["4", "6", "8", "10"],
        "answer": "8"
    },
    {
        "question": "Chemical symbol for gold?",
        "options": ["Go", "Gd", "Au", "Ag"],
        "answer": "Au"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    user_answer = input("Your answer (1-4): ")
    if q["options"][int(user_answer)-1] == q["answer"]:
        score += 1

print(f"Your final score: {score}/{len(questions)}")
