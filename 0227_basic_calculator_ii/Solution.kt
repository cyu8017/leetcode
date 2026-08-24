// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

class Solution {
    fun calculate(s: String): Int {
        val stack = ArrayDeque<Int>()
        var number = 0
        var operator = '+'

        for (index in s.indices) {
            val ch = s[index]
            if (ch.isDigit()) {
                number = number * 10 + (ch - '0')
            }
            if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || index == s.lastIndex) {
                when (operator) {
                    '+' -> stack.addLast(number)
                    '-' -> stack.addLast(-number)
                    '*' -> stack.addLast(stack.removeLast() * number)
                    '/' -> stack.addLast(stack.removeLast() / number)
                }
                operator = ch
                number = 0
            }
        }

        return stack.sum()
    }
}
