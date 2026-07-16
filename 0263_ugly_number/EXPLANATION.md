# How We Solve Ugly Number

Repeatedly remove factors of 2, 3, and 5 until none remain.

## Steps

1. Reject non-positive numbers.
2. While divisible by 2, divide by 2.
3. Repeat for 3 and then 5.
4. If the remaining value is 1, the number is ugly.
5. Otherwise return false.
