"""
main.py

Entry point for the Mini Quiz App.

This is a command-line quiz application that:
- Displays questions one at a time
- Accepts and checks the user's answers
- Tracks the score
- Shows the correct answer when the user is wrong
- Displays a final score and performance message

Game logic will be added in upcoming commits.
"""

from questions import QUESTIONS


def display_question(question_data, question_number, total_questions):
    """
    Displays a single question along with its options.

    question_data: a dictionary with keys "question", "options", "answer", "category"
    question_number: the current question's position (e.g. 1, 2, 3...)
    total_questions: the total number of questions being asked
    """
    print(f"\nQuestion {question_number}/{total_questions}  [{question_data['category']}]")
    print(question_data["question"])
    print()

    # options is a dictionary like {"A": "Stack", "B": "Queue", ...}
    for letter, option_text in question_data["options"].items():
        print(f"{letter}. {option_text}")


def get_user_answer():
    """
    Prompts the user for an answer and returns it as an uppercase letter.
    """
    user_input = input("\nYour answer: ")
    return user_input.strip().upper()


def check_answer(question_data, user_answer, current_score, question_number):
    """
    Checks whether the user's answer is correct, prints feedback in the
    format: "Correct! | Score: X/Y" or shows the correct answer if wrong.

    Returns the updated score.
    """
    correct_answer = question_data["answer"]

    if user_answer == correct_answer:
        current_score += 1
        print(f"\nCorrect! | Score: {current_score}/{question_number}")
    else:
        correct_text = question_data["options"][correct_answer]
        print(f"\nWrong! The correct answer was {correct_answer}. {correct_text}")
        print(f"Score: {current_score}/{question_number}")

    return current_score


def main():
    print("Welcome to the Mini Quiz App!")

    score = 0

    # Temporary: just test with the first question for now.
    first_question = QUESTIONS[0]
    display_question(first_question, 1, len(QUESTIONS))
    answer = get_user_answer()
    score = check_answer(first_question, answer, score, 1)
    # Looping through all questions will be added in Commit 6.


if __name__ == "__main__":
    main()