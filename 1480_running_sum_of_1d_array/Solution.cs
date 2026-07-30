// LeetCode 1480 - Running Sum Of 1d Array
// https://leetcode.com/problems/running-sum-of-1d-array/

public class Solution {
    public int[] RunningSum(int[] nums) {
        for (int i = 1; i < nums.Length; i++) nums[i] += nums[i - 1];
        return nums;
    }
}
