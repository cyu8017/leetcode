// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

public class Solution {
    public int Rob(int[] nums) {
        if (nums.Length == 1) {
            return nums[0];
        }
        return System.Math.Max(RobLinear(nums, 0, nums.Length - 1), RobLinear(nums, 1, nums.Length));
    }

    private static int RobLinear(int[] nums, int start, int end) {
        var previousTwo = 0;
        var previousOne = 0;
        for (var i = start; i < end; i++) {
            var current = System.Math.Max(previousOne, previousTwo + nums[i]);
            previousTwo = previousOne;
            previousOne = current;
        }
        return previousOne;
    }
}
