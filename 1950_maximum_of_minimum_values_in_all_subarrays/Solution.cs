// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindMaximums(int[] nums) {
        int n = nums.Length;
        var left = new int[n];
        var right = new int[n];
        var stack = new Stack<int>();
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack.Peek()] >= nums[i]) stack.Pop();
            left[i] = stack.Count > 0 ? stack.Peek() : -1;
            stack.Push(i);
        }
        stack.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && nums[stack.Peek()] >= nums[i]) stack.Pop();
            right[i] = stack.Count > 0 ? stack.Peek() : n;
            stack.Push(i);
        }
        var ans = new int[n];
        for (int i = 0; i < n; i++) {
            int length = right[i] - left[i] - 1;
            ans[length - 1] = Math.Max(ans[length - 1], nums[i]);
        }
        for (int i = n - 2; i >= 0; i--)
            ans[i] = Math.Max(ans[i], ans[i + 1]);
        return ans;
    }
}