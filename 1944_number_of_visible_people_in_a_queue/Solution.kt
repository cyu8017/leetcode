// LeetCode 1944
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

class Solution {
    fun canSeePersonsCount(heights: IntArray): IntArray {
        val n = heights.size
        val ans = IntArray(n)
        val stack = ArrayDeque<Int>()
        for (i in n - 1 downTo 0) {
            var count = 0
            while (stack.isNotEmpty() && heights[i] > stack.last()) {
                stack.removeLast()
                count++
            }
            if (stack.isNotEmpty()) count++
            ans[i] = count
            stack.addLast(heights[i])
        }
        return ans
    }
}
