// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

using System.Collections.Generic;

public class Solution {
    public bool ParseBoolExpr(string expression) {
        var stack = new List<char>();
        foreach (char ch in expression) {
            if (ch == ')') {
                var values = new List<bool>();
                while (stack.Count > 0 && stack[stack.Count - 1] != '&' &&
                       stack[stack.Count - 1] != '|' && stack[stack.Count - 1] != '!') {
                    char token = stack[stack.Count - 1];
                    stack.RemoveAt(stack.Count - 1);
                    if (token == 't' || token == 'f') {
                        values.Add(token == 't');
                    }
                }
                char op = stack[stack.Count - 1];
                stack.RemoveAt(stack.Count - 1);
                if (op == '!') {
                    stack.Add(values[0] ? 'f' : 't');
                } else if (op == '&') {
                    bool all = true;
                    foreach (bool v in values) {
                        all = all && v;
                    }
                    stack.Add(all ? 't' : 'f');
                } else {
                    bool any = false;
                    foreach (bool v in values) {
                        any = any || v;
                    }
                    stack.Add(any ? 't' : 'f');
                }
            } else if (ch != ',') {
                stack.Add(ch);
            }
        }
        return stack[stack.Count - 1] == 't';
    }
}
