// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

using System.Collections.Generic;

public class Solution {
    public bool ValidateStackSequences(int[] pushed, int[] popped) {
        var stack = new List<int>();
        int j = 0;
        foreach (int x in pushed) {
            stack.Add(x);
            while (stack.Count > 0 && stack[stack.Count - 1] == popped[j]) {
                stack.RemoveAt(stack.Count - 1);
                j++;
            }
        }
        return stack.Count == 0;
    }
}
