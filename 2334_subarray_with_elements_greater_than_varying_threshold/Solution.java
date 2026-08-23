// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int validSubarraySize(int[] nums, int threshold) {
        int n = nums.length;
        int[] left = new int[n], right = new int[n];
        var stack = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            while (stack.size() > 0 && nums[stack[stack.size() - 1]] >= nums[i]) stack.remove(stack.size() - 1);
            left[i] = stack.size() == 0 ? -1 : stack[stack.size() - 1];
            stack.add(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stack.size() > 0 && nums[stack[stack.size() - 1]] >= nums[i]) stack.remove(stack.size() - 1);
            right[i] = stack.size() == 0 ? n : stack[stack.size() - 1];
            stack.add(i);
        }
        for (int i = 0; i < n; i++) {
            int k = right[i] - left[i] - 1;
            if (nums[i] > threshold / k) return k;
        }
        return -1;
    }
}
