// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution {
    public boolean splitString(String s) {
        return dfs(s, 0, -1, 0);
    }

    private boolean dfs(String s, int index, long previous, int parts) {
        int n = s.length();
        if (index == n) {
            return parts >= 2;
        }

        for (int end = index + 1; end <= n; end++) {
            long value = Long.parseLong(s.substring(index, end));
            if (previous == -1) {
                if (dfs(s, end, value, parts + 1)) {
                    return true;
                }
            } else if (value == previous - 1) {
                if (dfs(s, end, value, parts + 1)) {
                    return true;
                }
            } else if (value > previous - 1) {
                break;
            }
        }

        return false;
    }
}
