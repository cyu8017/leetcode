# How We Solve Maximum Subarray

Find the contiguous chunk of numbers with the biggest sum.

## Steps

1. Start with the first number as both the current sum and best sum.
2. Move to the next number.
3. Either extend the current chunk (add the number) or start fresh at this number.
4. Update the best sum if the current chunk is bigger.
5. Repeat until the end of the list.
6. Return the best sum.
