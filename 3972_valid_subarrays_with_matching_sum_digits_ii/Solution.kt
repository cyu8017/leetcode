// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

class Solution {
    fun countValidSubarrays(nums: IntArray, x: Int): Long {
        val byRemainder = Array(10) { ArrayList<Long>() }
        byRemainder[0].add(0L)
        var prefix = 0L
        var answer = 0L
        for (value in nums) {
            prefix += value
            val required = ((prefix - x) % 10 + 10).toInt() % 10
            val values = byRemainder[required]
            var power = 1L
            while (x.toLong() * power <= prefix) {
                val low = x.toLong() * power
                val high = (x + 1).toLong() * power - 1
                val minPrefix = prefix - high
                val maxPrefix = prefix - low
                val left = lowerBound(values, minPrefix)
                val right = upperBound(values, maxPrefix)
                answer += right - left
                if (power > prefix / 10) break
                power *= 10
            }
            byRemainder[(prefix % 10).toInt()].add(prefix)
        }
        return answer
    }

    private fun lowerBound(a: ArrayList<Long>, x: Long): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (a[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }

    private fun upperBound(a: ArrayList<Long>, x: Long): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (a[mid] <= x) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
