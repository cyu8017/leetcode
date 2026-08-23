// LeetCode 0053 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

public class Solution {
    public int MaxSubArray(int[] nums) {
        int best = nums[0];
        int current = nums[0];

        for (int i = 1; i < nums.Length; i++) {
            current = Math.Max(nums[i], current + nums[i]);
            best = Math.Max(best, current);
        }

        return best;
    }
}
