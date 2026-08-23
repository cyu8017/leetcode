// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

using System;

public class Solution {
    public int MaximizeSum(int[] nums, int k) {
        int mx = nums[0];
        foreach (int x in nums) if (x > mx) mx = x;
        return k * mx + k * (k - 1) / 2;
    }
}
