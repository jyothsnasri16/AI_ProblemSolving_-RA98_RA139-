from itertools import permutations
import time

def solve_cryptarithm():
    start_time = time.time()
    
    letters = 'SENDMORY'
    digits = range(10)
    attempts = 0

    for perm in permutations(digits, len(letters)):
        attempts += 1
        s, e, n, d, m, o, r, y = perm

        if s == 0 or m == 0:
            continue

        send = 1000*s + 100*e + 10*n + d
        more = 1000*m + 100*o + 10*r + e
        money = 10000*m + 1000*o + 100*n + 10*e + y

        if send + more == money:
            print("✅ Solution Found:")
            print(f"S={s}, E={e}, N={n}, D={d}, M={m}, O={o}, R={r}, Y={y}")
            print(f"{send} + {more} = {money}")
            break

    end_time = time.time()
    print(f"\nAttempts: {attempts}")
    print(f"Time taken: {round(end_time - start_time, 2)} seconds")

solve_cryptarithm()