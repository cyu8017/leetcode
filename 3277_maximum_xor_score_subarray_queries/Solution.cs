// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

using System;

public class Solution {
    public int[] MaximumSubarrayXor(int[] nums, int[][] queries) {
        int n = nums.Length;
        int[][] f = new int[n][];
        for (int i = 0; i < n; i++) f[i] = new int[n];
        for (int i = 0; i < n; i++) f[i][i] = nums[i];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                f[i][j] = f[i][j - 1] ^ f[i + 1][j];
            }
        }
        int[][] best = new int[n][];
        for (int i = 0; i < n; i++) best[i] = new int[n];
        for (int i = 0; i < n; i++) best[i][i] = f[i][i];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                best[i][j] = Math.Max(f[i][j], Math.Max(best[i][j - 1], best[i + 1][j]));
            }
        }
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) ans[i] = best[queries[i][0]][queries[i][1]];
        return ans;
    }
}
