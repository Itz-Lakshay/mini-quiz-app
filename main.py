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


def main():
    print("Welcome to the Mini Quiz App!")

    # Temporary: just test with the first question for now.
    first_question = QUESTIONS[0]
    display_question(first_question, 1, len(QUESTIONS))
    answer = get_user_answer()
    print(f"\nYou answered: {answer}")
    # Answer checking will be added in the next commit.


if __name__ == "__main__":
    main()