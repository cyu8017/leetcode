// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

class Solution {
    fun clumsy(n: Int): Int {
        val stack = ArrayDeque<Int>()
        var cur = n
        stack.addLast(cur--)
        var op = 0
        while (cur > 0) {
            when (op % 4) {
                0 -> stack.addLast(stack.removeLast() * cur)
                1 -> stack.addLast(stack.removeLast() / cur)
                2 -> stack.addLast(cur)
                else -> stack.addLast(-cur)
            }
            cur--
            op++
        }
        return stack.sum()
    }
}
