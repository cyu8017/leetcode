// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

// JavaScript problem; C# stand-in.
public class Solution {
    public int Last(int[] nums) {
        if (nums == null || nums.Length == 0) return -1;
        return nums[nums.Length - 1];
    }
}
