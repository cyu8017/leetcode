// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate_valid_expressions/

class Solution {
    private String expression;

    public long evaluateExpression(String expression) {
        this.expression = expression;
        return parse(0)[0];
    }

    // returns {value, nextIndex}
    private long[] parse(int i) {
        char ch = expression.charAt(i);
        if (Character.isDigit(ch) || ch == '-') {
            int j = i;
            if (expression.charAt(j) == '-') j++;
            while (j < expression.length() && Character.isDigit(expression.charAt(j))) j++;
            return new long[]{Long.parseLong(expression.substring(i, j)), j};
        }
        int j = i;
        while (expression.charAt(j) != '(') j++;
        String op = expression.substring(i, j);
        j++;
        long[] p1 = parse(j);
        j = (int) p1[1] + 1;
        long[] p2 = parse(j);
        j = (int) p2[1] + 1;
        long res = 0;
        if (op.equals("add")) res = p1[0] + p2[0];
        else if (op.equals("sub")) res = p1[0] - p2[0];
        else if (op.equals("mul")) res = p1[0] * p2[0];
        else if (op.equals("div")) res = p1[0] / p2[0];
        return new long[]{res, j};
    }
}
