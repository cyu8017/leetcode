// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count_distinct_integers_after_removing_zeros/

class Solution {
    private String s;
    private int m;
    private long[][][][] f;

    public long countDistinct(long n) {
        s = Long.toString(n);
        m = s.length();
        f = new long[20][2][2][2];
        for (int i = 0; i < 20; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 2; k++)
                    for (int t = 0; t < 2; t++)
                        f[i][j][k][t] = -1;
        return dfs(0, 0, 1, 1);
    }

    private long dfs(int i, int zero, int lead, int limit) {
        if (i == m) return (zero == 0 && lead == 0) ? 1 : 0;
        if (limit == 0 && f[i][zero][lead][limit] != -1) return f[i][zero][lead][limit];
        int up = limit == 1 ? s.charAt(i) - '0' : 9;
        long ans = 0;
        for (int d = 0; d <= up; d++) {
            int nxtZero = zero;
            if (d == 0 && lead == 0) nxtZero = 1;
            int nxtLead = (lead == 1 && d == 0) ? 1 : 0;
            int nxtLimit = (limit == 1 && d == up) ? 1 : 0;
            ans += dfs(i + 1, nxtZero, nxtLead, nxtLimit);
        }
        if (limit == 0) f[i][zero][lead][limit] = ans;
        return ans;
    }
}
