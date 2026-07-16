// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

using System.Collections.Generic;

public class Solution {
    public bool Find132pattern(int[] nums) {
        Stack<int> stack = new();
        int third = int.MinValue;
        for (int i = nums.Length - 1; i >= 0; i--) {
            if (nums[i] < third) {
                return true;
            }
            while (stack.Count > 0 && nums[i] > stack.Peek()) {
                third = stack.Pop();
            }
            stack.Push(nums[i]);
        }
        return false;
    }
}
