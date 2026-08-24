// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

import java.util.*;

class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        List<Integer> stack = new ArrayList<>();
        int j = 0;
        for (int x : pushed) {
            stack.add(x);
            while (!stack.isEmpty() && stack.get(stack.size() - 1) == popped[j]) {
                stack.remove(stack.size() - 1);
                j++;
            }
        }
        return stack.isEmpty();
    }
}
