// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution {
    fun mctFromLeafValues(arr: IntArray): Int {
        val stack = ArrayDeque<Int>()
        stack.addLast(Int.MAX_VALUE)
        var ans = 0
        for (x in arr) {
            while (stack.last() <= x) {
                val mid = stack.removeLast()
                ans += mid * minOf(stack.last(), x)
            }
            stack.addLast(x)
        }
        while (stack.size > 2) {
            ans += stack.removeLast() * stack.last()
        }
        return ans
    }
}
