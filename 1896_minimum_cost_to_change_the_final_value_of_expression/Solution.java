// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

class Solution {
    private String expression;
    private int index;

    public int minOperationsToFlip(String expression) {
        this.expression = expression;
        this.index = 0;
        int[] result = parseExpr();
        return result[0] == 0 ? result[2] : result[1];
    }

    private int[] parseExpr() {
        int[] node = parseFactor();
        while (index < expression.length()
                && (expression.charAt(index) == '&' || expression.charAt(index) == '|')) {
            char op = expression.charAt(index++);
            node = combine(node, op, parseFactor());
        }
        return node;
    }

    private int[] parseFactor() {
        if (expression.charAt(index) == '0' || expression.charAt(index) == '1') {
            int value = expression.charAt(index++) - '0';
            int toZero = value == 0 ? 0 : 1;
            int toOne = value == 0 ? 1 : 0;
            return new int[] {value, toZero, toOne};
        }
        index++;
        int[] node = parseExpr();
        index++;
        return node;
    }

    private int[] combine(int[] left, char op, int[] right) {
        int leftVal = left[0];
        int leftToZero = left[1];
        int leftToOne = left[2];
        int rightVal = right[0];
        int rightToZero = right[1];
        int rightToOne = right[2];

        if (op == '&') {
            int andVal = leftVal & rightVal;
            int andToZero = Math.min(leftToZero, leftToOne + rightToZero);
            int andToOne = leftToOne + rightToOne;
            int orToZero = leftToZero + rightToZero;
            int orToOne = Math.min(leftToOne, Math.min(leftToZero + rightToOne, rightToZero + leftToOne));
            int val = andVal;
            int toZero = Math.min(andToZero, 1 + orToZero);
            int toOne = Math.min(andToOne, 1 + orToOne);
            return new int[] {val, toZero, toOne};
        }

        int orVal = leftVal | rightVal;
        int orToZero = leftToZero + rightToZero;
        int orToOne = Math.min(leftToOne, Math.min(leftToZero + rightToOne, rightToZero + leftToOne));
        int andToZero = Math.min(leftToZero, leftToOne + rightToZero);
        int andToOne = leftToOne + rightToOne;
        int val = orVal;
        int toZero = Math.min(orToZero, 1 + andToZero);
        int toOne = Math.min(orToOne, 1 + andToOne);
        return new int[] {val, toZero, toOne};
    }
}
