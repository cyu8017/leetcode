// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

public class Solution {
    public int FindLengthOfLCIS(int[] nums) {
        int best = 1, cur = 1;
        for (int i = 1; i < nums.Length; ++i) {
            if (nums[i] > nums[i - 1]) {
                ++cur;
                if (cur > best) best = cur;
            } else {
                cur = 1;
            }
        }
        return best;
    }
}
