// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean verifyPreorder(int[] preorder) {
        long low = Long.MIN_VALUE;
        Deque<Integer> stack = new ArrayDeque<>();

        for (int value : preorder) {
            if (value < low) {
                return false;
            }
            while (!stack.isEmpty() && stack.peekLast() < value) {
                low = stack.removeLast();
            }
            stack.addLast(value);
        }

        return true;
    }
}
