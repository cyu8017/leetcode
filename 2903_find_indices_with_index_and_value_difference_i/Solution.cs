// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

using System;

public class Solution {
    public int[] FindIndices(int[] nums, int indexDifference, int valueDifference) {
        int n = nums.Length;
        for (int i = 0; i < n; i++)
            for (int j = i; j < n; j++) {
                int di = Math.Abs(j - i), dv = Math.Abs(nums[i] - nums[j]);
                if (di >= indexDifference && dv >= valueDifference) return new[] { i, j };
            }
        return new[] { -1, -1 };
    }
}
