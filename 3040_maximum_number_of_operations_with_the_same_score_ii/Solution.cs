// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

using System;

public class Solution {
    public int MaxOperations(int[] nums) {
        int n = nums.Length;
        int G(int i0, int j0, int s) {
            int[][] f = new int[n][];
            for (int i = 0; i < n; i++) {
                f[i] = new int[n];
                for (int j = 0; j < n; j++) f[i][j] = -1;
            }
            int Dfs(int i, int j) {
                if (j - i < 1) return 0;
                if (f[i][j] != -1) return f[i][j];
                int ans = 0;
                if (nums[i] + nums[i + 1] == s) ans = Math.Max(ans, 1 + Dfs(i + 2, j));
                if (nums[i] + nums[j] == s) ans = Math.Max(ans, 1 + Dfs(i + 1, j - 1));
                if (nums[j - 1] + nums[j] == s) ans = Math.Max(ans, 1 + Dfs(i, j - 2));
                return f[i][j] = ans;
            }
            return Dfs(i0, j0);
        }
        int a = G(2, n - 1, nums[0] + nums[1]);
        int b = G(0, n - 3, nums[n - 1] + nums[n - 2]);
        int c = G(1, n - 2, nums[0] + nums[n - 1]);
        return 1 + Math.Max(a, Math.Max(b, c));
    }
}
