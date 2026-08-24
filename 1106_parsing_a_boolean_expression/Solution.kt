// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution {
    fun parseBoolExpr(expression: String): Boolean {
        val stack = ArrayDeque<Char>()
        for (ch in expression) {
            if (ch == ')') {
                val values = mutableListOf<Boolean>()
                while (stack.isNotEmpty() && stack.last() !in "&|!") {
                    val token = stack.removeLast()
                    if (token == 't' || token == 'f') values.add(token == 't')
                }
                val op = stack.removeLast()
                when (op) {
                    '!' -> stack.addLast(if (!values[0]) 't' else 'f')
                    '&' -> stack.addLast(if (values.all { it }) 't' else 'f')
                    else -> stack.addLast(if (values.any { it }) 't' else 'f')
                }
            } else if (ch != ',') {
                stack.addLast(ch)
            }
        }
        return stack.last() == 't'
    }
}
