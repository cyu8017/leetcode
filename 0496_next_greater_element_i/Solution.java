// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> nextGreater = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int num : nums2) {
            while (!stack.isEmpty() && stack.peek() < num) {
                nextGreater.put(stack.pop(), num);
            }
            stack.push(num);
        }
        int[] result = new int[nums1.length];
        for (int index = 0; index < nums1.length; index++) {
            result[index] = nextGreater.getOrDefault(nums1[index], -1);
        }
        return result;
    }
}
