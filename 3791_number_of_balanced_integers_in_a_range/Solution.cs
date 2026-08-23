// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

public class Solution {
    const int BASE = 90;
    string num;
    long[,] f = new long[20, 181];

    long Dfs(int pos, int diff, bool lim) {
        if (pos >= num.Length) return diff == 0 ? 1 : 0;
        if (!lim && f[pos, diff + BASE] != -1) return f[pos, diff + BASE];
        int up = lim ? num[pos] - '0' : 9;
        long res = 0;
        for (int i = 0; i <= up; i++) {
            if (pos % 2 == 0) res += Dfs(pos + 1, diff + i, lim && i == up);
            else res += Dfs(pos + 1, diff - i, lim && i == up);
        }
        if (!lim) f[pos, diff + BASE] = res;
        return res;
    }

    void ClearF() {
        for (int i = 0; i < 20; i++)
            for (int j = 0; j < 181; j++)
                f[i, j] = -1;
    }

    public long CountBalanced(long low, long high) {
        if (high < 11) return 0;
        if (low < 11) low = 11;
        num = (low - 1).ToString();
        ClearF();
        long a = Dfs(0, 0, true);
        num = high.ToString();
        ClearF();
        long b = Dfs(0, 0, true);
        return b - a;
    }
}
