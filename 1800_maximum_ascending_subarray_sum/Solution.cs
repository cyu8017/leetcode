// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/

public class Solution {
    public int MaxAscendingSum(int[] nums) {
        int best = nums[0];
        int cur = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] > nums[i - 1]) {
                cur += nums[i];
            } else {
                cur = nums[i];
            }
            best = Math.Max(best, cur);
        }
        return best;
    }
}
