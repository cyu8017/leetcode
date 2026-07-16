// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class Solution {
    public List<String> removeInvalidParentheses(String s) {
        Set<String> result = new HashSet<>();
        Queue<String> queue = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        queue.offer(s);
        visited.add(s);
        boolean found = false;
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int step = 0; step < levelSize; step++) {
                String current = queue.poll();
                if (isValid(current)) {
                    result.add(current);
                    found = true;
                }
                if (found) {
                    continue;
                }
                for (int index = 0; index < current.length(); index++) {
                    char ch = current.charAt(index);
                    if (ch != '(' && ch != ')') {
                        continue;
                    }
                    String next = current.substring(0, index) + current.substring(index + 1);
                    if (visited.add(next)) {
                        queue.offer(next);
                    }
                }
            }
        }
        return new ArrayList<>(result);
    }

    private boolean isValid(String text) {
        int balance = 0;
        for (int index = 0; index < text.length(); index++) {
            char ch = text.charAt(index);
            if (ch == '(') {
                balance++;
            } else if (ch == ')') {
                if (balance == 0) {
                    return false;
                }
                balance--;
            }
        }
        return balance == 0;
    }
}
