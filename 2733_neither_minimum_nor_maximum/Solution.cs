// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

using System;

public class Solution {
    public int FindNonMinOrMax(int[] nums) {
        if (nums.Length < 3) return -1;
        int a = nums[0], b = nums[1], c = nums[2];
        return a + b + c - Math.Max(a, Math.Max(b, c)) - Math.Min(a, Math.Min(b, c));
    }
}
