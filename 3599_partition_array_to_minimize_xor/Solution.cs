// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

using System;

public class Solution {
    public int MinXor(int[] nums, int k) {
        int n = nums.Length;
        int[] g = new int[n + 1];
        for (int i = 1; i <= n; i++) g[i] = g[i - 1] ^ nums[i - 1];
        const int Inf = int.MaxValue / 2;
        int[][] f = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
            f[i] = new int[k + 1];
            for (int j = 0; j <= k; j++) f[i][j] = Inf;
        }
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= Math.Min(i, k); j++) {
                for (int h = j - 1; h < i; h++) {
                    f[i][j] = Math.Min(f[i][j], Math.Max(f[h][j - 1], g[i] ^ g[h]));
                }
            }
        }
        return f[n][k];
    }
}
