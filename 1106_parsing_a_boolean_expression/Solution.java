// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

import java.util.*;

class Solution {
    public boolean parseBoolExpr(String expression) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : expression.toCharArray()) {
            if (ch == ')') {
                List<Boolean> values = new ArrayList<>();
                while (!stack.isEmpty() && stack.peek() != '&' && stack.peek() != '|' && stack.peek() != '!') {
                    char token = stack.pop();
                    if (token == 't' || token == 'f') {
                        values.add(token == 't');
                    }
                }
                char op = stack.pop();
                if (op == '!') {
                    stack.push(values.get(0) ? 'f' : 't');
                } else if (op == '&') {
                    boolean all = true;
                    for (boolean v : values) all &= v;
                    stack.push(all ? 't' : 'f');
                } else {
                    boolean any = false;
                    for (boolean v : values) any |= v;
                    stack.push(any ? 't' : 'f');
                }
            } else if (ch != ',') {
                stack.push(ch);
            }
        }
        return stack.peek() == 't';
    }
}
