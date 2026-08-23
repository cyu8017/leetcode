// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

using System;

public class Solution {
    public int MaximumProcessableQueries(int[] nums, int[] queries) {
        int n = nums.Length;
        int[][] f = new int[n][];
        for (int i = 0; i < n; i++) f[i] = new int[n];
        int m = queries.Length;
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j >= i; j--) {
                if (i > 0) {
                    int t = f[i - 1][j] < m && nums[i - 1] >= queries[f[i - 1][j]] ? 1 : 0;
                    f[i][j] = Math.Max(f[i][j], f[i - 1][j] + t);
                }
                if (j + 1 < n) {
                    int t = f[i][j + 1] < m && nums[j + 1] >= queries[f[i][j + 1]] ? 1 : 0;
                    f[i][j] = Math.Max(f[i][j], f[i][j + 1] + t);
                }
                if (f[i][j] == m) return m;
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int t = f[i][i] < m && nums[i] >= queries[f[i][i]] ? 1 : 0;
            ans = Math.Max(ans, f[i][i] + t);
        }
        return ans;
    }
}
