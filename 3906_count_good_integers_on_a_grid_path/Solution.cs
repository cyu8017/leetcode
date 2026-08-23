// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

using System;

public class Solution {
    public long CountGoodIntegersOnPath(long l, long r, string directions) {
        var key = new bool[16];
        int row = 0, col = 0;
        key[0] = true;
        foreach (char c in directions) {
            if (c == 'D') row++;
            else col++;
            key[row * 4 + col] = true;
        }

        string s = "";
        var f = new long[16][];
        for (int i = 0; i < 16; i++) f[i] = new long[10];

        long Dfs(int pos, int last, bool lim) {
            if (pos == 16) return 1;
            if (!lim && f[pos][last] != -1) return f[pos][last];
            long res = 0;
            int start = key[pos] ? last : 0;
            int end = lim ? (s[pos] - '0') : 9;
            for (int i = start; i <= end; i++) {
                int nextLast = key[pos] ? i : last;
                res += Dfs(pos + 1, nextLast, lim && (i == end));
            }
            if (!lim) f[pos][last] = res;
            return res;
        }

        long Calc(long x) {
            if (x < 0) return 0;
            string t = x.ToString();
            s = new string('0', 16 - t.Length) + t;
            for (int i = 0; i < 16; i++)
                for (int j = 0; j < 10; j++) f[i][j] = -1;
            return Dfs(0, 0, true);
        }

        return Calc(r) - Calc(l - 1);
    }
}
