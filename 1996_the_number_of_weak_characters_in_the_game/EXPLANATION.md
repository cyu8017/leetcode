# Approach
Sort by attack asc, defense desc; scan from right tracking max defense — a character is weak if a later (higher attack) has greater defense.

# Complexity
Time O(n log n). Space O(1).
