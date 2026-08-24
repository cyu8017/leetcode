// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/


class Solution {
    fun findKthNumber(m: Int, n: Int, k: Int): Int {
        var left = 1
        var right = m * n
        while (left < right) {
            val mid = (left + right) / 2
            if (count(m, n, mid) >= k) right = mid else left = mid + 1
        }
        return left
    }

    private fun count(m: Int, n: Int, x: Int): Int {
        var total = 0
        for (i in 1..m) total += minOf(n, x / i)
        return total
    }
}
