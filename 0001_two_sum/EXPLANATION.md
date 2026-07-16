# How We Solve Two Sum

You have a list of numbers. Find **two numbers** that add up to a target.

## Steps

1. Look at each number one at a time.
2. For each number, ask: "What friend number do I need to reach the target?"
3. Keep a notebook (hash map) of numbers you already saw and where they are.
4. If the friend number is in the notebook, you found the answer.
5. If not, write this number in the notebook and keep going.
6. Return the two positions of the pair.
