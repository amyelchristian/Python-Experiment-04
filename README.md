# Experiment 04 — User Defined Functions

A set of five Python programs practising user-defined functions across a range of problem types.

---

## Problems

### Problem 01 — Divisibility Check
[problem01.py](problem01.py)

Accepts a number and checks if it is divisible by 7 using a user-defined function. Prints whether or not the number passes the test.

### Problem 02 — Name Prefix (Mr/Ms)
[problem02.py](problem02.py)

Accepts a name and gender code (`M` or `F`) and returns the name with the correct prefix (`Mr.` or `Ms.`). Handles unrecognized inputs gracefully.

### Problem 03 — Quadratic Equation Discriminant
[problem03.py](problem03.py)

Takes the coefficients `a`, `b`, and `c` of a quadratic equation and computes the discriminant (`b² - 4ac`). Reports whether the equation has two real roots, one real root, or no real roots. Guards against `a = 0`.

### Problem 04 — Lucky Draw (Random Module)
[problem04.py](problem04.py)

Simulates a lucky draw for ABC School's Annual Day. Randomly selects a winning token number from 1 to 600 using Python's `random` module, with a short delay added for effect via the `time` module.

### Problem 05 — Compound Interest Calculator
[problem05.py](problem05.py)

Calculates compound interest using the formula `CI = P * (1 + r/n)^(nt)`. Accepts principal, annual interest rate, time (years), and compounding frequency as inputs, then displays the total amount and the interest earned.

---

## How to Run

Each file is standalone. Run any problem from the terminal:

```bash
python problem01.py
```

No external dependencies are required — only Python's standard library (`random`, `time`).
