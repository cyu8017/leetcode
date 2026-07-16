# How We Solve Divide Two Integers

Divide without using * or / (use bits instead).

## Steps

1. Handle overflow special case (MIN / -1).
2. Remember if the answer should be negative.
3. Work with positive absolute values.
4. For each bit position, if dividend is big enough, subtract (divisor << bit) and add (1 << bit) to quotient.
5. Return quotient with the correct sign.
