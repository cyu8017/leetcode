// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution {
    public int maximizeSum(int[] nums, int k) {
        int mx = nums[0];
        for (int x : nums) if (x > mx) mx = x;
        return k * mx + k * (k - 1) / 2;
    }
}
