# Approach
For each index, find the longest subarray where it is the minimum (monotonic stack). That value is a candidate for answer[length-1]. Propagate maxima from longer lengths down to shorter ones.

# Complexity
Time O(n). Space O(n).
