// LeetCode 0976 - Largest Perimeter Triangle
// https://leetcode.com/problems/largest-perimeter-triangle/

using System;

public class Solution {
    public int LargestPerimeter(int[] nums) {
        Array.Sort(nums);
        Array.Reverse(nums);
        for (int i = 0; i + 2 < nums.Length; i++) {
            if (nums[i] < nums[i + 1] + nums[i + 2])
                return nums[i] + nums[i + 1] + nums[i + 2];
        }
        return 0;
    }
}
