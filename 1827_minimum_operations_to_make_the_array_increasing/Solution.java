// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution {
    public int minOperations(int[] nums) {
        int ops = 0;
        int prev = nums[0];
        for (int index = 1; index < nums.length; index++) {
            int value = nums[index];
            if (value <= prev) {
                int needed = prev + 1;
                ops += needed - value;
                prev = needed;
            } else {
                prev = value;
            }
        }
        return ops;
    }
}
