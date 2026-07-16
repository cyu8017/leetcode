// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

public class Solution {
    public bool VerifyPreorder(int[] preorder) {
        long low = long.MinValue;
        var stack = new Stack<int>();

        foreach (int value in preorder) {
            if (value < low) {
                return false;
            }
            while (stack.Count > 0 && stack.Peek() < value) {
                low = stack.Pop();
            }
            stack.Push(value);
        }

        return true;
    }
}
