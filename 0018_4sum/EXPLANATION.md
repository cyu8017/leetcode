# How We Solve 4Sum

Find four numbers that add to a target (like 3Sum with one more loop).

## Steps

1. Sort the list.
2. Pick first number i, then second number j.
3. Use left and right fingers for the last two numbers.
4. Skip duplicate i and j values.
5. When sum matches target, save and skip duplicate left/right values.
6. Return all unique quadruples.
