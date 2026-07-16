# How We Solve Implement Rand10() Using Rand7()

Use rejection sampling on pairs of `rand7()` calls to cover a uniform range up to 40.

## Steps

1. Form `num = (rand7() - 1) * 7 + rand7()` to get 1..49 uniformly.
2. Reject values above 40 to avoid bias.
3. Map accepted values to 1..10 with modulo arithmetic.
