// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        int n = nums.length;
        int m = multipliers.length;
        int[] next = new int[m + 1];
        for (int i = m - 1; i >= 0; i--) {
            int[] cur = new int[m + 1];
            for (int left = i; left >= 0; left--) {
                int right = n - 1 - (i - left);
                int takeLeft = nums[left] * multipliers[i] + next[left + 1];
                int takeRight = nums[right] * multipliers[i] + next[left];
                cur[left] = Math.max(takeLeft, takeRight);
            }
            next = cur;
        }
        return next[0];
    }
}
