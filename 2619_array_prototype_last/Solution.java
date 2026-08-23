// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

class Solution {
    public int last(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        return nums[nums.length - 1];
    }
}
