import json

with open("file/questions.json") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternatives in enumerate(question["alternatives"]):
        print(index + 1, "-", alternatives)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


for question in data:
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "correct answer"
    else:
        result = "wrong answer"
    message = f"{result} - your answer: {question['user_choice']} / correct answer: {question['correct_answer']}"
    print(message)

print(score)

