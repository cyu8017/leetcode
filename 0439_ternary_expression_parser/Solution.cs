// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

public class Solution {
    public string ParseTernary(string expression) {
        if (!expression.Contains('?')) {
            return expression;
        }

        int separator = 2;
        int depth = 0;
        for (int index = 2; index < expression.Length; index++) {
            char ch = expression[index];
            if (ch == '?') {
                depth++;
            } else if (ch == ':') {
                if (depth == 0) {
                    separator = index;
                    break;
                }
                depth--;
            }
        }

        if (expression[0] == 'T') {
            return ParseTernary(expression.Substring(2, separator - 2));
        }
        return ParseTernary(expression.Substring(separator + 1));
    }
}
