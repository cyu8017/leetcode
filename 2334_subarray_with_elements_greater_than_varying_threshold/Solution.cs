// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

using System.Collections.Generic;

public class Solution {
    public int ValidSubarraySize(int[] nums, int threshold) {
        int n = nums.Length;
        int[] left = new int[n], right = new int[n];
        var stack = new List<int>();
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack[stack.Count - 1]] >= nums[i]) stack.RemoveAt(stack.Count - 1);
            left[i] = stack.Count == 0 ? -1 : stack[stack.Count - 1];
            stack.Add(i);
        }
        stack.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && nums[stack[stack.Count - 1]] >= nums[i]) stack.RemoveAt(stack.Count - 1);
            right[i] = stack.Count == 0 ? n : stack[stack.Count - 1];
            stack.Add(i);
        }
        for (int i = 0; i < n; i++) {
            int k = right[i] - left[i] - 1;
            if (nums[i] > threshold / k) return k;
        }
        return -1;
    }
}
