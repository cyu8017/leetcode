// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

public class Solution {
    public int[] NextGreaterElements(int[] nums) {
        int length = nums.Length;
        int[] result = new int[length];
        for (int index = 0; index < length; index++) {
            result[index] = -1;
        }
        Stack<int> stack = new();
        for (int index = 0; index < length * 2; index++) {
            int value = nums[index % length];
            while (stack.Count > 0 && nums[stack.Peek()] < value) {
                result[stack.Pop()] = value;
            }
            if (index < length) {
                stack.Push(index);
            }
        }
        return result;
    }
}
