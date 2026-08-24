// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

class Solution {
    fun calculate(s: String): Int {
        val expr = StringBuilder()
        for (ch in s) if (!ch.isWhitespace()) expr.append(ch)
        val i = intArrayOf(0)
        return parse(expr.toString(), i)
    }

    private fun parse(expr: String, i: IntArray): Int {
        val stack = ArrayList<Long>()
        var num = 0L
        var sign = '+'
        while (i[0] < expr.length) {
            val ch = expr[i[0]]
            if (ch.isDigit()) num = num * 10 + (ch - '0')
            else if (ch == '(') {
                i[0]++
                num = parse(expr, i).toLong()
            }
            if ((!ch.isDigit() && ch != '(') || i[0] == expr.length - 1) {
                if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')' || i[0] == expr.length - 1) {
                    when (sign) {
                        '+' -> stack.add(num)
                        '-' -> stack.add(-num)
                        '*' -> stack[stack.size - 1] = stack[stack.size - 1] * num
                        '/' -> {
                            val top = stack.removeAt(stack.size - 1)
                            stack.add((top.toDouble() / num).toLong())
                        }
                    }
                    if (ch == ')') {
                        var sum = 0L
                        for (v in stack) sum += v
                        return sum.toInt()
                    }
                    sign = ch
                    num = 0
                }
            }
            i[0]++
        }
        var total = 0L
        for (v in stack) total += v
        return total.toInt()
    }
}
