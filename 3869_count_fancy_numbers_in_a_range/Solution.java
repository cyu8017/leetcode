// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

import java.util.Arrays;

class Solution {
    private String num;
    private long[][][][] f;
    private int n;

    private static boolean check(int s) {
        if (s < 100) return s % 11 != 0;
        int mid = (s / 10) % 10;
        int last = s % 10;
        return mid > 1 && mid < last;
    }

    public long countFancy(long l, long r) {
        return calc(r) - calc(l - 1);
    }

    private long calc(long x) {
        num = Long.toString(x);
        n = num.length();
        f = new long[n][9 * n + 1][10][4];
        for (int i = 0; i < n; i++)
            for (int j = 0; j <= 9 * n; j++)
                for (int p = 0; p < 10; p++)
                    Arrays.fill(f[i][j][p], -1);
        return dfs(0, 0, 0, 0, true);
    }

    private long dfs(int pos, int s, int prev, int st, boolean lim) {
        if (pos >= n) {
            if (st != 3) return 1;
            return check(s) ? 1 : 0;
        }
        if (!lim && f[pos][s][prev][st] != -1) return f[pos][s][prev][st];
        int up = lim ? num.charAt(pos) - '0' : 9;
        long res = 0;
        for (int i = 0; i <= up; i++) {
            int nxtSt = st;
            if (st == 0) {
                if (prev == 0) nxtSt = 0;
                else if (i > prev) nxtSt = 1;
                else if (i < prev) nxtSt = 2;
                else nxtSt = 3;
            } else if (st == 1) {
                nxtSt = i > prev ? 1 : 3;
            } else if (st == 2) {
                nxtSt = i < prev ? 2 : 3;
            } else {
                nxtSt = 3;
            }
            res += dfs(pos + 1, s + i, i, nxtSt, lim && i == up);
        }
        if (!lim) f[pos][s][prev][st] = res;
        return res;
    }
}
