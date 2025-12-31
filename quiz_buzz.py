""" Quiz Buzz App """
import json

""" Extract questionnaire from quiz_questions.json file"""
with open("files/quiz_questions.json", 'r') as file:
    content = file.read()

questions = json.loads(content)
user_response = []

try:
    for question in questions:
        
        """ Print Question Details """
        print(question["question_text"])
        print("Options:")

        for index, option in enumerate(question["alternatives"]):
            print(f"{index + 1}. {option}")
        
        stringified_user_input = input("Enter option number:")
        user_input = int(stringified_user_input)

        isCorrect = False

        if user_input == question["correct_answer"]:
            isCorrect = True

        response = {}

        response["question_id"] = question["question_id"]
        response["user_answer"] = int(user_input)
        response["correct_answer"] = question["correct_answer"]
        response["is_correct"] = isCorrect
        
        user_response.append(response)

    total_score = 0

    print("\n***Result***\n")

    for response in user_response:
    
        print(f"Question No. - {response['question_id']} : User Answer - {response['user_answer']} : Correct Answer - {response['correct_answer']}")

        if response["is_correct"] == True:
            total_score = total_score + 1

    print(f"\nYour Score: {total_score} / {len(questions)}\n")

except ValueError:
    print('Invalid Value!')
    print('Start the quiz again!')