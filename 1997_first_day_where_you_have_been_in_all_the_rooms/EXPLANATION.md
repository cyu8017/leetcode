# Approach
`dp[i]` = day first reaching room i. From i-1 you revisit nextVisit[i-1] then return; recurrence `2*dp[i-1] - dp[nextVisit[i-1]] + 2`.

# Complexity
Time O(n). Space O(n).
