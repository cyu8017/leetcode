// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number_of_balanced_integers_in_a_range/

import java.util.Arrays;

class Solution {
    private static final int BASE = 90;
    private String num;
    private long[][] f = new long[20][181];

    private long dfs(int pos, int diff, boolean lim) {
        if (pos >= num.length()) return diff == 0 ? 1 : 0;
        if (!lim && f[pos][diff + BASE] != -1) return f[pos][diff + BASE];
        int up = lim ? num.charAt(pos) - '0' : 9;
        long res = 0;
        for (int i = 0; i <= up; i++) {
            if (pos % 2 == 0) res += dfs(pos + 1, diff + i, lim && i == up);
            else res += dfs(pos + 1, diff - i, lim && i == up);
        }
        if (!lim) f[pos][diff + BASE] = res;
        return res;
    }

    public long countBalanced(long low, long high) {
        if (high < 11) return 0;
        if (low < 11) low = 11;
        num = Long.toString(low - 1);
        for (long[] row : f) Arrays.fill(row, -1);
        long a = dfs(0, 0, true);
        num = Long.toString(high);
        for (long[] row : f) Arrays.fill(row, -1);
        long b = dfs(0, 0, true);
        return b - a;
    }
}
