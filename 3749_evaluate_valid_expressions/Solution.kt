// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate_valid_expressions/

class Solution {
    private var expression: String? = null

    fun evaluateExpression(expression: String): Long {
        this.expression = expression
        return parse(0)[0]
    }

    // returns {value, nextIndex}
    private fun parse(i: Int): LongArray {
        var ch = expression[i]
        if (ch.isDigit() || ch == '-') {
            var j = i
            if (expression[j] == '-') { j = j + 1 }
            while (j < expression.length && expression[j].isDigit()) { j += 1 }
            return longArrayOf(expression.substring(i, j.toLong()), j)
        }
        var j = i
        while (expression[j] != '(') { j += 1 }
        var op = expression.substring(i, j)
        j = j + 1
        var p1 = parse(j)
        j = p1[1] + 1
        var p2 = parse(j)
        j = p2[1] + 1
        var res = 0
        if ((op == "add")) res = p1[0] + p2[0]
        else if ((op == "sub")) res = p1[0] - p2[0]
        else if ((op == "mul")) res = p1[0] * p2[0]
        else if ((op == "div")) res = p1[0] / p2[0]
        return longArrayOf(res, j)
    }
}
