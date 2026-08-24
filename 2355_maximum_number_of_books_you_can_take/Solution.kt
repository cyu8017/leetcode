// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

import java.util.ArrayDeque

class Solution {
    fun maximumBooks(books: IntArray): Long {
        val n = books.size
        val dp = LongArray(n)
        val stack = ArrayDeque<Int>()
        var ans = 0L
        for (i in 0 until n) {
            while (stack.isNotEmpty() && books[stack.peek()] >= books[i] - (i - stack.peek())) {
                stack.pop()
            }
            if (stack.isEmpty()) {
                dp[i] = sum(0, i, books[i])
            } else {
                val j = stack.peek()
                dp[i] = dp[j] + sum(j + 1, i, books[i])
            }
            ans = maxOf(ans, dp[i])
            stack.push(i)
        }
        return ans
    }

    private fun sum(l: Int, r: Int, h: Int): Long {
        val width = r - l + 1
        return if (h >= width) width.toLong() * (2L * h - width + 1) / 2
        else h.toLong() * (h + 1) / 2
    }
}
