# Approach
Monotonic decreasing stack from the right. Pop everyone shorter (each is visible), then if anyone remains they are the next taller visible person.

# Complexity
Time O(n). Space O(n).
