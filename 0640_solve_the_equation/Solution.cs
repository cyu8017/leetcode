// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

public class Solution {
    public string SolveEquation(string equation) {
        int eq = equation.IndexOf('=');
        var (leftCoef, leftConst) = Parse(equation.Substring(0, eq));
        var (rightCoef, rightConst) = Parse(equation.Substring(eq + 1));
        int coef = leftCoef - rightCoef;
        int constant = rightConst - leftConst;
        if (coef == 0) return constant == 0 ? "Infinite solutions" : "No solution";
        return "x=" + (constant / coef);
    }

    private (int coef, int constant) Parse(string expr) {
        int coef = 0, constant = 0, n = expr.Length, i = 0;
        while (i < n) {
            int sign = 1;
            if (expr[i] == '+' || expr[i] == '-') {
                sign = expr[i] == '-' ? -1 : 1;
                ++i;
            }
            int value = 0;
            bool hasDigit = false;
            while (i < n && char.IsDigit(expr[i])) {
                hasDigit = true;
                value = value * 10 + (expr[i] - '0');
                ++i;
            }
            if (i < n && expr[i] == 'x') {
                coef += sign * (hasDigit ? value : 1);
                ++i;
            } else {
                constant += sign * value;
            }
        }
        return (coef, constant);
    }
}
