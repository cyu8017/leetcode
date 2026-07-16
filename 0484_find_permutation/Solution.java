// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

class Solution {
    public int[] findPermutation(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        List<Integer> result = new ArrayList<>();
        stack.push(1);
        for (char ch : s.toCharArray()) {
            if (ch == 'I') {
                while (!stack.isEmpty()) {
                    result.add(stack.pop());
                }
            }
            stack.push(stack.size() + result.size() + 1);
        }
        while (!stack.isEmpty()) {
            result.add(stack.pop());
        }
        int[] values = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            values[i] = result.get(i);
        }
        return values;
    }
}
