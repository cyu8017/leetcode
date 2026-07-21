// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution {
    fun maxValue(n: Int, index: Int, maxSum: Int): Int {
        fun minSideSum(value: Long, count: Long): Long {
            return if (value > count) {
                (value - 1 + value - count) * count / 2
            } else {
                value * (value - 1) / 2 + (count - value + 1)
            }
        }

        var lo = 1L
        var hi = maxSum.toLong()
        while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            val total = minSideSum(mid, index.toLong()) + mid + minSideSum(mid, (n - index - 1).toLong())
            if (total <= maxSum) lo = mid else hi = mid - 1
        }
        return lo.toInt()
    }
}
