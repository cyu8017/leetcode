// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

using System;

public class Solution {
    public int MaxScore(int[] nums) {
        int n = nums.Length;
        int[] f = new int[n];
        int Dfs(int i) {
            if (f[i] > 0) return f[i];
            for (int j = i + 1; j < n; j++) {
                f[i] = Math.Max(f[i], (j - i) * nums[j] + Dfs(j));
            }
            return f[i];
        }
        return Dfs(0);
    }
}
