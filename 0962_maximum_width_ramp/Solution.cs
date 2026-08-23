// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxWidthRamp(int[] nums) {
        var stack = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (stack.Count == 0 || nums[stack[stack.Count - 1]] > nums[i]) stack.Add(i);
        }
        int ans = 0;
        for (int j = nums.Length - 1; j >= 0; j--) {
            while (stack.Count > 0 && nums[stack[stack.Count - 1]] <= nums[j]) {
                ans = Math.Max(ans, j - stack[stack.Count - 1]);
                stack.RemoveAt(stack.Count - 1);
            }
        }
        return ans;
    }
}
