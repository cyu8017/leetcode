// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

class Solution {
    fun calPoints(operations: Array<String>): Int {
        var stack = ArrayList<Int>()
        for (op in operations) {
            if ((op == "C")) stack.removeAt(stack.size - 1)
            else if ((op == "D")) stack.add(stack[stack.size - 1] * 2)
            else if ((op == "+")) stack.add(stack[stack.size - 1] + stack[stack.size - 2])
            else stack.add(op.toInt())
        }
        var total = 0
        for (value in stack) { total += value }
        return total
    }
}
