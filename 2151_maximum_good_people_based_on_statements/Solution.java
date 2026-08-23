// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

class Solution {
    private boolean ok(int[][] statements, int n, int mask) {
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) continue;
            for (int j = 0; j < n; j++) {
                int s = statements[i][j];
                if (s == 2) continue;
                boolean goodJ = (mask & (1 << j)) != 0;
                if ((s == 1 && !goodJ) || (s == 0 && goodJ)) return false;
            }
        }
        return true;
    }

    public int maximumGood(int[][] statements) {
        int n = statements.length, ans = 0;
        for (int mask = 0; mask < (1 << n); mask++)
            if (ok(statements, n, mask)) ans = Math.max(ans, Integer.bitCount(mask));
        return ans;
    }
}
