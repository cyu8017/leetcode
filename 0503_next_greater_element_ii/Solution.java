// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int length = nums.length;
        int[] result = new int[length];
        for (int index = 0; index < length; index++) {
            result[index] = -1;
        }
        Deque<Integer> stack = new ArrayDeque<>();
        for (int index = 0; index < length * 2; index++) {
            int value = nums[index % length];
            while (!stack.isEmpty() && nums[stack.peek()] < value) {
                result[stack.pop()] = value;
            }
            if (index < length) {
                stack.push(index);
            }
        }
        return result;
    }
}
