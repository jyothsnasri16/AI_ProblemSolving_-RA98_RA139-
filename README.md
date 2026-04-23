# Crypt Arithmetic Puzzle Solver (CSP)

## Problem Description

This project solves crypt arithmetic puzzles where each letter represents a unique digit (0–9).
The objective is to find a correct mapping such that the given arithmetic equation is satisfied.

Example:
SEND + MORE = MONEY

---

## Algorithm Used

Constraint Satisfaction Problem (CSP) using permutation-based approach.

---

## CSP Representation

* Variables: Letters in the puzzle
* Domain: Digits (0–9)
* Constraints:

  * Each letter must have a unique digit
  * No leading digit should be zero
  * The arithmetic equation must be correct

---

## Execution Steps

1. Take input puzzle (WORD+WORD=RESULT)
2. Extract all unique letters
3. Generate permutations of digits
4. Assign digits to letters
5. Check constraints
6. Verify equation
7. Display the solution

---

## Features

* Accepts dynamic user input (not hardcoded)
* GUI-based interface using Tkinter
* Displays solution, attempts, and execution time
* Handles invalid input

---

## How to Run

Run the following command:
python crypt_gui.py

Enter puzzle in format:
WORD+WORD=RESULT

Example:
SEND+MORE=MONEY

Click **Solve** to get the result.

---

## Sample Output

9567 + 1085 = 10652
S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2

---

## Project Structure

CryptArithmetic/
│
├── crypt_solver.py
├── crypt_gui.py
└── README.md

---

## Author

Your Name : Jyothsna Sri Priya
Register Number : RA2411026050098
