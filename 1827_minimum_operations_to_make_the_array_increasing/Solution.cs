// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

public class Solution {
    public int MinOperations(int[] nums) {
        int ops = 0;
        int prev = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] <= prev) {
                int needed = prev + 1;
                ops += needed - nums[i];
                prev = needed;
            } else {
                prev = nums[i];
            }
        }
        return ops;
    }
}
