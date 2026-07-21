// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

public class Solution {
    private string expression = "";
    private int index;

    public int MinOperationsToFlip(string expression) {
        this.expression = expression;
        index = 0;
        int[] node = ParseExpr();
        return node[0] == 0 ? node[2] : node[1];
    }

    private static int[] Combine(int[] left, char op, int[] right) {
        int leftVal = left[0], leftToZero = left[1], leftToOne = left[2];
        int rightVal = right[0], rightToZero = right[1], rightToOne = right[2];
        if (op == '&') {
            int andVal = leftVal & rightVal;
            int andToZero = Math.Min(leftToZero, leftToOne + rightToZero);
            int andToOne = leftToOne + rightToOne;
            int orToZero = leftToZero + rightToZero;
            int orToOne = Math.Min(leftToOne, Math.Min(leftToZero + rightToOne, rightToZero + leftToOne));
            return new[] { andVal, Math.Min(andToZero, 1 + orToZero), Math.Min(andToOne, 1 + orToOne) };
        } else {
            int orVal = leftVal | rightVal;
            int orToZero = leftToZero + rightToZero;
            int orToOne = Math.Min(leftToOne, Math.Min(leftToZero + rightToOne, rightToZero + leftToOne));
            int andToZero = Math.Min(leftToZero, leftToOne + rightToZero);
            int andToOne = leftToOne + rightToOne;
            return new[] { orVal, Math.Min(orToZero, 1 + andToZero), Math.Min(orToOne, 1 + andToOne) };
        }
    }

    private int[] ParseFactor() {
        if (expression[index] == '0' || expression[index] == '1') {
            int value = expression[index] - '0';
            index++;
            return new[] { value, value == 0 ? 0 : 1, value == 0 ? 1 : 0 };
        }
        index++;
        int[] node = ParseExpr();
        index++;
        return node;
    }

    private int[] ParseExpr() {
        int[] node = ParseFactor();
        while (index < expression.Length && (expression[index] == '&' || expression[index] == '|')) {
            char op = expression[index];
            index++;
            node = Combine(node, op, ParseFactor());
        }
        return node;
    }
}
