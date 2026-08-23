// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

class Solution {
    public String parseTernary(String expression) {
        if (!expression.contains("?")) {
            return expression;
        }

        int separator = 2;
        int depth = 0;
        for (int index = 2; index < expression.length(); index++) {
            char ch = expression.charAt(index);
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

        if (expression.charAt(0) == 'T') {
            return parseTernary(expression.substring(2, separator));
        }
        return parseTernary(expression.substring(separator + 1));
    }
}
