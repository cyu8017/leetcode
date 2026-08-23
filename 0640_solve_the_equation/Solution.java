// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

class Solution {
    public String solveEquation(String equation) {
        int eq = equation.indexOf('=');
        int[] left = parse(equation.substring(0, eq));
        int[] right = parse(equation.substring(eq + 1));
        int coef = left[0] - right[0];
        int constant = right[1] - left[1];
        if (coef == 0) {
            return constant == 0 ? "Infinite solutions" : "No solution";
        }
        return "x=" + (constant / coef);
    }

    private int[] parse(String expr) {
        int coef = 0;
        int constant = 0;
        int n = expr.length();
        int i = 0;
        while (i < n) {
            int sign = 1;
            if (expr.charAt(i) == '+' || expr.charAt(i) == '-') {
                sign = expr.charAt(i) == '-' ? -1 : 1;
                ++i;
            }
            int value = 0;
            boolean hasDigit = false;
            while (i < n && Character.isDigit(expr.charAt(i))) {
                hasDigit = true;
                value = value * 10 + (expr.charAt(i) - '0');
                ++i;
            }
            if (i < n && expr.charAt(i) == 'x') {
                coef += sign * (hasDigit ? value : 1);
                ++i;
            } else {
                constant += sign * value;
            }
        }
        return new int[] {coef, constant};
    }
}
