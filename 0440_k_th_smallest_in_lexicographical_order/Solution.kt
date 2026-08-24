// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution {
    fun findKthNumber(n: Int, k: Int): Int {
        var current = 1
        var remaining = k - 1

        while (remaining > 0) {
            val steps = countSteps(n, current.toLong(), current + 1L)
            if (steps <= remaining) {
                current++
                remaining -= steps.toInt()
            } else {
                current *= 10
                remaining--
            }
        }

        return current
    }

    private fun countSteps(n: Int, first: Long, last: Long): Long {
        var steps = 0L
        var currentFirst = first
        var currentLast = last
        while (currentFirst <= n) {
            steps += minOf(n + 1L, currentLast) - currentFirst
            currentFirst *= 10
            currentLast *= 10
        }
        return steps
    }
}
