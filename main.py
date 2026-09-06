"""
main.py

Entry point for the Mini Quiz App.

This is a command-line quiz application that:
- Displays questions one at a time
- Accepts and checks the user's answers
- Tracks the score
- Shows the correct answer when the user is wrong
- Displays a final score and performance message
"""

import time
import random
from questions import QUESTIONS

TIME_LIMIT_SECONDS = 15
HIGH_SCORE_FILE = "highscore.txt"


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

    for letter, option_text in question_data["options"].items():
        print(f"{letter}. {option_text}")


def get_user_answer(valid_options):
    """
    Prompts the user for an answer and keeps asking until they enter
    a valid option letter. Returns the answer as an uppercase letter.

    valid_options: an iterable of valid letters, e.g. dict_keys(["A", "B", "C", "D"])
    """
    while True:
        user_input = input("\nYour answer: ").strip().upper()

        if user_input in valid_options:
            return user_input

        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")


def check_answer(question_data, user_answer, current_score, question_number, time_taken):
    """
    Checks whether the user's answer is correct and within the time limit.
    Prints feedback in the format: "Correct! | Score: X/Y", or shows the
    correct answer if wrong or if the user ran out of time.

    Returns the updated score.
    """
    correct_answer = question_data["answer"]
    ran_out_of_time = time_taken > TIME_LIMIT_SECONDS

    if user_answer == correct_answer and not ran_out_of_time:
        current_score += 1
        print(f"\nCorrect! | Score: {current_score}/{question_number}")
    else:
        correct_text = question_data["options"][correct_answer]
        if ran_out_of_time:
            print(f"\nTime's up! The correct answer was {correct_answer}. {correct_text}")
        else:
            print(f"\nWrong! The correct answer was {correct_answer}. {correct_text}")
        print(f"Score: {current_score}/{question_number}")

    return current_score


def get_performance_message(percentage):
    """
    Returns a performance message based on the percentage of correct answers.
    """
    if percentage == 100:
        return "Perfect score! You're a quiz master!"
    elif percentage >= 80:
        return "Excellent work!"
    elif percentage >= 60:
        return "Good job! Keep practicing."
    elif percentage >= 40:
        return "Not bad, but there's room for improvement."
    else:
        return "Keep learning — you'll do better next time!"


def display_final_score(score, total_questions):
    """
    Displays the final score and a performance message.
    """
    percentage = (score / total_questions) * 100
    message = get_performance_message(percentage)

    print("\n" + "=" * 30)
    print("QUIZ COMPLETE!")
    print(f"Final Score: {score}/{total_questions} ({percentage:.1f}%)")
    print(message)
    print("=" * 30)


def run_quiz(questions):
    """
    Runs the full quiz: loops through every question, displays it,
    collects the user's answer within a time limit, checks it, and
    tracks the score.

    Questions are shuffled so each playthrough has a different order.

    Returns the final score.
    """
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)

    score = 0
    total_questions = len(shuffled_questions)

    for index, question_data in enumerate(shuffled_questions, start=1):
        display_question(question_data, index, total_questions)
        print(f"(You have {TIME_LIMIT_SECONDS} seconds to answer)")

        start_time = time.time()
        answer = get_user_answer(question_data["options"].keys())
        time_taken = time.time() - start_time

        score = check_answer(question_data, answer, score, index, time_taken)

    return score

def get_available_categories(questions):
    """
    Returns a sorted list of unique categories found in the questions.
    """
    categories = set()
    for question_data in questions:
        categories.add(question_data["category"])
    return sorted(categories)


def choose_category(questions):
    """
    Asks the user to pick a category to play, or all categories.
    Returns the filtered list of questions for the chosen category.
    """
    categories = get_available_categories(questions)

    print("\nAvailable categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")
    print(f"{len(categories) + 1}. All Categories")

    while True:
        choice = input("\nChoose a category (enter the number): ").strip()

        if choice.isdigit():
            choice_number = int(choice)

            if 1 <= choice_number <= len(categories):
                selected_category = categories[choice_number - 1]
                return [q for q in questions if q["category"] == selected_category]

            if choice_number == len(categories) + 1:
                return questions

        print("Invalid choice. Please enter a valid number from the list.")

def load_high_score():
    """
    Reads the high score from the high score file.
    Returns 0 if the file doesn't exist yet or is invalid.
    """
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            content = file.read().strip()
            return int(content) if content else 0
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


def save_high_score(score):
    """
    Saves the given score to the high score file.
    """
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))

def main():
    print("Welcome to the Mini Quiz App!")

    high_score = load_high_score()
    print(f"Current High Score: {high_score}")

    selected_questions = choose_category(QUESTIONS)
    final_score = run_quiz(selected_questions)
    display_final_score(final_score, len(selected_questions))

    if final_score > high_score:
        print(f"\nNew High Score! You beat the previous record of {high_score}!")
        save_high_score(final_score)
    else:
        print(f"\nHigh Score remains: {high_score}")


if __name__ == "__main__":
    main()