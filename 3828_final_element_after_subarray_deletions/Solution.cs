// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

using System;

public class Solution {
    public int FinalElement(int[] nums) {
        return Math.Max(nums[0], nums[nums.Length - 1]);
    }
}
