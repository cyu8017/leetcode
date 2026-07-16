# How We Solve Shifting Letters

Suffix sums of shifts: later shifts also affect earlier letters.

## Steps

1. Walk right to left accumulating `shifts[i]`.
2. Shift each character by the running total modulo 26.
3. Join into the result string.
