# How We Solve Integer to English Words

Convert three-digit chunks and append scale words.

## Steps

1. Return `Zero` for input 0.
2. Split the number into chunks of up to three digits.
3. Convert each chunk with ones, tens, and hundreds rules.
4. Attach Thousand, Million, or Billion labels as needed.
5. Join the chunk phrases in order.
