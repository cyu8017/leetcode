// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/


class Solution {
    fun solveEquation(equation: String): String {
        val parts = equation.split("=")
        val left = parse(parts[0])
        val right = parse(parts[1])
        val coeff = left.first - right.first
        val const = right.second - left.second
        return when {
            coeff == 0 && const == 0 -> "Infinite solutions"
            coeff == 0 -> "No solution"
            else -> "x=${const / coeff}"
        }
    }

    private fun parse(expr: String): Pair<Int, Int> {
        var coeff = 0
        var const = 0
        var i = 0
        val n = expr.length
        while (i < n) {
            var sign = 1
            if (expr[i] == '+' || expr[i] == '-') {
                if (expr[i] == '-') sign = -1
                i++
            }
            var value = 0
            var hasNum = false
            while (i < n && expr[i].isDigit()) {
                hasNum = true
                value = value * 10 + (expr[i] - '0')
                i++
            }
            if (i < n && expr[i] == 'x') {
                coeff += sign * (if (hasNum) value else 1)
                i++
            } else {
                const += sign * value
            }
        }
        return coeff to const
    }
}
