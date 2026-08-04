// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

class Solution {
    fun makeArrayIncreasing(arr1: IntArray, arr2: IntArray): Int {
        val sorted = arr2.toSortedSet().toList()
        var dp = mutableMapOf(-1 to 0)
        for (num in arr1) {
            val next = mutableMapOf<Int, Int>()
            for ((prev, ops) in dp) {
                if (num > prev) {
                    next[num] = minOf(next.getOrDefault(num, Int.MAX_VALUE), ops)
                }
                val idx = upperBound(sorted, prev)
                if (idx < sorted.size) {
                    val chosen = sorted[idx]
                    next[chosen] = minOf(next.getOrDefault(chosen, Int.MAX_VALUE), ops + 1)
                }
            }
            dp = next
            if (dp.isEmpty()) return -1
        }
        return dp.values.minOrNull() ?: -1
    }

    private fun upperBound(a: List<Int>, target: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] <= target) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
