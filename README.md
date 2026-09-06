# Mini Quiz App

A command-line quiz application built in Python for the ACE (Association of
Computer Enthusiasts) society submission.

## Overview

This is a terminal-based quiz game that tests the user's knowledge across
multiple categories, with a live score tracker, a per-question timer, and a
persistent high-score system.

## Features

- 11 quiz questions across 3 categories (DSA, Python, General Knowledge),
  stored separately from the game logic
- Displays one question at a time and accepts the user's answer
- Tracks score live and shows the correct answer when the user is wrong
- Displays a final score and a performance message at the end
- Input validation — keeps prompting until a valid option is entered
- **Bonus:** randomized question order each playthrough
- **Bonus:** category selection (play one category or all of them)
- **Bonus:** a 15-second timer per question
- **Bonus:** a persistent high-score system saved across runs
- Graceful exit on Ctrl+C

## How to Run

```bash
python main.py
```

## Project Structure

```
mini-quiz-app/
├── main.py         # Game logic: display, input, scoring, game loop
├── questions.py     # Question data, stored separately from game logic
├── highscore.txt    # Auto-generated to store the high score (not tracked in Git)
├── .gitignore
└── README.md
```

## Skills Demonstrated

- **Data structures:** questions stored as a list of dictionaries, with
  nested dictionaries for answer options
- **Functions:** the entire app is broken into small, single-purpose
  functions (display, input, scoring, validation, file I/O)
- **Control flow:** loops for the quiz and input validation, conditionals
  for scoring and performance messages
- **Modular programming:** question data and game logic are kept in
  separate files

## Example Output

```
Question 3/11  [DSA]
Which data structure follows FIFO?

A. Stack
B. Queue
C. Tree
D. Graph
(You have 15 seconds to answer)

Your answer: B

Correct! | Score: 3/3
```

## Possible Future Improvements

- A true real-time countdown that cuts off input mid-typing (would require
  threading or OS-specific input handling)
- Storing high scores per category instead of a single overall high score
- Exporting quiz results to a file