# How We Solve Median of Two Sorted Arrays

Two sorted lists join into one big sorted list. Find the **middle value**.

## Steps

1. Binary search on the shorter list to pick a cut.
2. Cut the other list so left parts have the same total size.
3. Check: biggest on left <= smallest on right (for both lists).
4. If not, move the cut and try again.
5. When it fits, the median comes from the edge values of the cuts.
6. Return that number (average if even total length).
