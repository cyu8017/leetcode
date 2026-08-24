// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

class StockSpanner {
    private val stack = mutableListOf<IntArray>()

    fun next(price: Int): Int {
        var span = 1
        while (stack.isNotEmpty() && stack[stack.size - 1][0] <= price) {
            span += stack[stack.size - 1][1]
            stack.removeAt(stack.size - 1)
        }
        stack.add(intArrayOf(price, span))
        return span
    }
}
