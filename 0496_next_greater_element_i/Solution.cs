// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

public class Solution {
    public int[] NextGreaterElement(int[] nums1, int[] nums2) {
        Dictionary<int, int> nextGreater = new();
        Stack<int> stack = new();
        foreach (int num in nums2) {
            while (stack.Count > 0 && stack.Peek() < num) {
                nextGreater[stack.Pop()] = num;
            }
            stack.Push(num);
        }
        int[] result = new int[nums1.Length];
        for (int index = 0; index < nums1.Length; index++) {
            result[index] = nextGreater.GetValueOrDefault(nums1[index], -1);
        }
        return result;
    }
}
