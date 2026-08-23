// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int best = 1;
        int cur = 1;
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] > nums[i - 1]) {
                ++cur;
                best = Math.max(best, cur);
            } else {
                cur = 1;
            }
        }
        return best;
    }
}
