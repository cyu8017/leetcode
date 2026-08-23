// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

public class Solution {
    public int MaximumScore(int[] nums, int[] multipliers) {
        int n = nums.Length;
        int m = multipliers.Length;
        int[] next = new int[m + 1];
        for (int i = m - 1; i >= 0; i--) {
            int[] cur = new int[m + 1];
            for (int left = i; left >= 0; left--) {
                int right = n - 1 - (i - left);
                int takeLeft = nums[left] * multipliers[i] + next[left + 1];
                int takeRight = nums[right] * multipliers[i] + next[left];
                cur[left] = System.Math.Max(takeLeft, takeRight);
            }
            next = cur;
        }
        return next[0];
    }
}
