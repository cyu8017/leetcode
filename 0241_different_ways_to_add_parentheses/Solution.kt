// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution {
    fun diffWaysToCompute(expression: String): List<Int> {
        val result = mutableListOf<Int>()
        if (expression.all { it.isDigit() }) {
            return listOf(expression.toInt())
        }
        for (index in expression.indices) {
            val operator = expression[index]
            if (operator != '+' && operator != '-' && operator != '*') {
                continue
            }
            val left = diffWaysToCompute(expression.substring(0, index))
            val right = diffWaysToCompute(expression.substring(index + 1))
            for (leftValue in left) {
                for (rightValue in right) {
                    result.add(
                        when (operator) {
                            '+' -> leftValue + rightValue
                            '-' -> leftValue - rightValue
                            else -> leftValue * rightValue
                        }
                    )
                }
            }
        }
        return result
    }
}
