// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean find132pattern(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();
        int third = Integer.MIN_VALUE;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] < third) {
                return true;
            }
            while (!stack.isEmpty() && nums[i] > stack.peek()) {
                third = stack.pop();
            }
            stack.push(nums[i]);
        }
        return false;
    }
}
