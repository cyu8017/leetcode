// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

import java.util.*;

class Solution {
    public int[] findMaximums(int[] nums) {
        int n = nums.length;
        int[] left = new int[n], right = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) stack.pop();
            left[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) stack.pop();
            right[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int length = right[i] - left[i] - 1;
            ans[length - 1] = Math.max(ans[length - 1], nums[i]);
        }
        for (int i = n - 2; i >= 0; i--) ans[i] = Math.max(ans[i], ans[i + 1]);
        return ans;
    }
}
