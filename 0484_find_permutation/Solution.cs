// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

public class Solution {
    public int[] FindPermutation(string s) {
        Stack<int> stack = new();
        List<int> result = new();
        stack.Push(1);
        foreach (char ch in s) {
            if (ch == 'I') {
                while (stack.Count > 0) {
                    result.Add(stack.Pop());
                }
            }
            stack.Push(stack.Count + result.Count + 1);
        }
        while (stack.Count > 0) {
            result.Add(stack.Pop());
        }
        return result.ToArray();
    }
}
