// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

class Solution {
    fun parseTernary(expression: String): String {
        if ('?' !in expression) {
            return expression
        }

        var separator = 2
        var depth = 0
        for (index in 2 until expression.length) {
            when (expression[index]) {
                '?' -> depth++
                ':' -> {
                    if (depth == 0) {
                        separator = index
                        break
                    }
                    depth--
                }
            }
        }

        return if (expression[0] == 'T') {
            parseTernary(expression.substring(2, separator))
        } else {
            parseTernary(expression.substring(separator + 1))
        }
    }
}
