// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

using System;
using System.Collections.Generic;

public class Solution {
    public int TotalSteps(int[] nums) {
        var stack = new List<(int val, int steps)>();
        int ans = 0;
        for (int i = nums.Length - 1; i >= 0; i--) {
            int steps = 0;
            while (stack.Count > 0 && nums[i] > stack[stack.Count - 1].val) {
                steps = Math.Max(steps, stack[stack.Count - 1].steps);
                stack.RemoveAt(stack.Count - 1);
                steps++;
            }
            ans = Math.Max(ans, steps);
            stack.Add((nums[i], steps));
        }
        return ans;
    }
}
