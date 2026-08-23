// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

using System;

public class Solution {
    public int NumberOfPermutations(int n, int[][] requirements) {
        int[] req = new int[n];
        Array.Fill(req, -1);
        foreach (var r in requirements) req[r[0]] = r[1];
        if (req[0] > 0) return 0;
        req[0] = 0;
        int m = 0;
        foreach (int v in req) m = Math.Max(m, v);
        const int mod = 1000000007;
        int[][] f = new int[n][];
        for (int i = 0; i < n; i++) f[i] = new int[m + 1];
        f[0][0] = 1;
        for (int i = 1; i < n; i++) {
            int l = 0, r = m;
            if (req[i] >= 0) l = r = req[i];
            for (int j = l; j <= r; j++) {
                for (int k = 0; k <= Math.Min(i, j); k++) {
                    f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod;
                }
            }
        }
        return f[n - 1][req[n - 1]];
    }
}
