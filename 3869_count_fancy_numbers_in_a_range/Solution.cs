// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

using System;

public class Solution {
    static bool Check(int s) {
        if (s < 100) return s % 11 != 0;
        int mid = (s / 10) % 10;
        int last = s % 10;
        return mid > 1 && mid < last;
    }

    public long CountFancy(long l, long r) {
        long Calc(long x) {
            string num = x.ToString();
            int n = num.Length;
            var f = new long[n][][][];
            for (int i = 0; i < n; i++) {
                f[i] = new long[9 * n + 1][][];
                for (int j = 0; j <= 9 * n; j++) {
                    f[i][j] = new long[10][];
                    for (int p = 0; p < 10; p++) {
                        f[i][j][p] = new long[4];
                        Array.Fill(f[i][j][p], -1);
                    }
                }
            }
            long Dfs(int pos, int s, int prev, int st, bool lim) {
                if (pos >= n) {
                    if (st != 3) return 1;
                    return Check(s) ? 1 : 0;
                }
                if (!lim && f[pos][s][prev][st] != -1) return f[pos][s][prev][st];
                int up = lim ? num[pos] - '0' : 9;
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
                    res += Dfs(pos + 1, s + i, i, nxtSt, lim && i == up);
                }
                if (!lim) f[pos][s][prev][st] = res;
                return res;
            }
            return Dfs(0, 0, 0, 0, true);
        }
        return Calc(r) - Calc(l - 1);
    }
}
