"""
questions.py

This module stores all quiz questions separately from the main game logic.
Each question is stored as a dictionary with the following keys:
    - "question": the question text
    - "options": a dictionary of answer choices (A, B, C, D)
    - "answer": the correct option letter
    - "category": the topic/category this question belongs to
"""

QUESTIONS = [
    {
        "question": "Which data structure follows FIFO?",
        "options": {"A": "Stack", "B": "Queue", "C": "Tree", "D": "Graph"},
        "answer": "B",
        "category": "DSA",
    },
    {
        "question": "Which data structure follows LIFO?",
        "options": {"A": "Queue", "B": "Linked List", "C": "Stack", "D": "Array"},
        "answer": "C",
        "category": "DSA",
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": {"A": "O(n)", "B": "O(log n)", "C": "O(n^2)", "D": "O(1)"},
        "answer": "B",
        "category": "DSA",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"},
        "answer": "B",
        "category": "Python",
    },
    {
        "question": "Which of these is a mutable data type in Python?",
        "options": {"A": "tuple", "B": "string", "C": "list", "D": "int"},
        "answer": "C",
        "category": "Python",
    },
    {
        "question": "What does the 'len()' function do in Python?",
        "options": {
            "A": "Returns the type of an object",
            "B": "Returns the length of an object",
            "C": "Deletes an object",
            "D": "Returns the memory address",
        },
        "answer": "B",
        "category": "Python",
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {"A": "//", "B": "#", "C": "/*", "D": "--"},
        "answer": "B",
        "category": "Python",
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": {
            "A": "Alan Turing",
            "B": "Charles Babbage",
            "C": "Bill Gates",
            "D": "John von Neumann",
        },
        "answer": "B",
        "category": "General Knowledge",
    },
    {
        "question": "What does 'CPU' stand for?",
        "options": {
            "A": "Central Processing Unit",
            "B": "Computer Personal Unit",
            "C": "Central Program Unit",
            "D": "Control Processing Unit",
        },
        "answer": "A",
        "category": "General Knowledge",
    },
    {
        "question": "Which company developed the Python programming language?",
        "options": {
            "A": "Microsoft",
            "B": "It was created by Guido van Rossum, not a company",
            "C": "Google",
            "D": "Apple",
        },
        "answer": "B",
        "category": "General Knowledge",
    },
    {
        "question": "What is the smallest unit of data in a computer?",
        "options": {"A": "Byte", "B": "Nibble", "C": "Bit", "D": "Word"},
        "answer": "C",
        "category": "General Knowledge",
    },
]