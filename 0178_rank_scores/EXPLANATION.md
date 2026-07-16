# How We Solve Rank Scores

Use dense ranking so ties share a rank and the next rank is consecutive.

## Steps

1. Select each score from `Scores`.
2. Apply `DENSE_RANK()` ordered by score descending.
3. Alias the rank column as `rank`.
4. Order the output by score descending.
5. Return score and rank pairs.
