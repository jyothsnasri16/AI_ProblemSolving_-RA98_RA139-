import tkinter as tk
from itertools import permutations
import time
# CSP Representation:
# Variables: Letters in the puzzle
# Domain: Digits (0–9)
# Constraints:
# 1. Each letter must have a unique digit
# 2. No leading digit can be zero
# 3. The arithmetic equation must be satisfied

def solve_puzzle():
    puzzle = entry.get().replace(" ", "").upper()
    

    if "=" not in puzzle or "+" not in puzzle:
        output_label.config(text="❌ Use format: WORD+WORD=RESULT")
        return


    left, result = puzzle.split("=")
    words = left.split("+")

    # Collect all unique letters
    letters = set("".join(words) + result)

    if len(letters) > 10:
        output_label.config(text="❌ Too many unique letters (max 10)")
        return

    letters = list(letters)

    start_time = time.time()
    attempts = 0

    for perm in permutations(range(10), len(letters)):
        attempts += 1
        mapping = dict(zip(letters, perm))

        # Leading letters should not be zero
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue

        # Convert words to numbers
        nums = [int("".join(str(mapping[c]) for c in word)) for word in words]
        res = int("".join(str(mapping[c]) for c in result))

        if sum(nums) == res:
            end_time = time.time()

            solution_text = " + ".join(map(str, nums)) + " = " + str(res)
            mapping_text = ", ".join(f"{k}={v}" for k, v in mapping.items())

            output_label.config(
                text=f"✅ Solution:\n{solution_text}\n\nMapping:\n{mapping_text}\n\nAttempts: {attempts}\nTime: {round(end_time-start_time,2)} sec"
            )
            return

    output_label.config(text="❌ No solution found")

# GUI Setup
root = tk.Tk()
root.title("Crypt Arithmetic Solver")
root.geometry("450x350")

tk.Label(root, text="Enter Puzzle (e.g. WORD+WORD=RESULT)").pack(pady=10)

entry = tk.Entry(root, width=35)
entry.pack(pady=5)

tk.Button(root, text="Solve", command=solve_puzzle).pack(pady=10)

output_label = tk.Label(root, text="", fg="blue", wraplength=400, justify="left")
output_label.pack(pady=20)

root.mainloop()