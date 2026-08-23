// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution {
    public int punishmentNumber(int n) {
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int sq = i * i;
            if (can(sq, i)) ans += sq;
        }
        return ans;
    }

    private boolean can(int sq, int target) {
        String s = Integer.toString(sq);
        return dfs(s, 0, 0, target);
    }

    private boolean dfs(String s, int i, int sum, int target) {
        int m = s.length();
        if (i == m) return sum == target;
        int cur = 0;
        for (int j = i; j < m; j++) {
            cur = cur * 10 + (s.charAt(j) - '0');
            if (sum + cur > target) break;
            if (dfs(s, j + 1, sum + cur, target)) return true;
        }
        return false;
    }
}
