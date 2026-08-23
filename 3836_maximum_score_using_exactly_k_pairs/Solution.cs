// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

using System;

public class Solution {
    public long MaxScore(int[] nums1, int[] nums2, int K) {
        int n = nums1.Length, m = nums2.Length;
        const long NEG = long.MinValue / 4;
        var f = new long[n + 1][][];
        for (int i = 0; i <= n; i++) {
            f[i] = new long[m + 1][];
            for (int j = 0; j <= m; j++) {
                f[i][j] = new long[K + 1];
                Array.Fill(f[i][j], NEG);
            }
        }
        f[0][0][0] = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= K; k++) {
                    if (i > 0) f[i][j][k] = Math.Max(f[i][j][k], f[i - 1][j][k]);
                    if (j > 0) f[i][j][k] = Math.Max(f[i][j][k], f[i][j - 1][k]);
                    if (i > 0 && j > 0 && k > 0) {
                        f[i][j][k] = Math.Max(f[i][j][k], f[i - 1][j - 1][k - 1] + (long)nums1[i - 1] * nums2[j - 1]);
                    }
                }
            }
        }
        return f[n][m][K];
    }
}
