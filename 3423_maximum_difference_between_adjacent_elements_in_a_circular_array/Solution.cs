// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

using System;

public class Solution {
    public int MaxAdjacentDistance(int[] nums) {
        int ans = 0;
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            int d = Math.Abs(nums[i] - nums[(i + 1) % n]);
            if (d > ans) ans = d;
        }
        return ans;
    }
}
