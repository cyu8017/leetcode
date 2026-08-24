// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

class Solution {
    fun calculate(s: String): Int {
        val stack = ArrayDeque<Int>()
        var result = 0
        var number = 0
        var sign = 1
        for (ch in s) {
            when {
                ch.isDigit() -> number = number * 10 + (ch - '0')
                ch == '+' || ch == '-' -> {
                    result += sign * number
                    number = 0
                    sign = if (ch == '+') 1 else -1
                }
                ch == '(' -> {
                    stack.addLast(result)
                    stack.addLast(sign)
                    result = 0
                    sign = 1
                }
                ch == ')' -> {
                    result += sign * number
                    number = 0
                    result *= stack.removeLast()
                    result += stack.removeLast()
                }
            }
        }
        result += sign * number
        return result
    }
}
