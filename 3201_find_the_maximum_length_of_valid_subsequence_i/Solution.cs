// LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

using System;

public class Solution {
    public int MaximumLength(int[] nums) {
        int k = 2;
        int[][] f = new int[k][];
        for (int i = 0; i < k; i++) f[i] = new int[k];
        int ans = 0;
        foreach (int raw in nums) {
            int x = raw % k;
            for (int j = 0; j < k; j++) {
                int y = (j - x + k) % k;
                f[x][y] = f[y][x] + 1;
                ans = Math.Max(ans, f[x][y]);
            }
        }
        return ans;
    }
}
