// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int validSubarrays(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
                int j = stack.pop();
                ans += i - j;
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            int j = stack.pop();
            ans += nums.length - j;
        }
        return ans;
    }
}
