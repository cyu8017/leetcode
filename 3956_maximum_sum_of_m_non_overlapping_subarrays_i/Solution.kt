// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

class Solution {
    fun maxSum(nums: IntArray, m: Int, l: Int, r: Int): Long {
        val n = nums.size
        val prefix = LongArray(n + 1)
        for (i in 0 until n) prefix[i + 1] = prefix[i] + nums[i]
        var dp = LongArray(n + 1)
        var bestSelected = -(1L shl 62)
        for (count in 1..m) {
            val next = dp.copyOf()
            val deque = ArrayList<Int>()
            for (end in 1..n) {
                val addIndex = end - l
                if (addIndex >= 0) {
                    val value = dp[addIndex] - prefix[addIndex]
                    while (deque.isNotEmpty()) {
                        val last = deque[deque.size - 1]
                        if (dp[last] - prefix[last] > value) break
                        deque.removeAt(deque.size - 1)
                    }
                    deque.add(addIndex)
                }
                val minIndex = end - r
                while (deque.isNotEmpty() && deque[0] < minIndex) deque.removeAt(0)
                if (deque.isNotEmpty()) {
                    val candidate = prefix[end] + dp[deque[0]] - prefix[deque[0]]
                    if (candidate > next[end]) next[end] = candidate
                    if (candidate > bestSelected) bestSelected = candidate
                }
                if (next[end - 1] > next[end]) next[end] = next[end - 1]
            }
            dp = next
        }
        return bestSelected
    }
}
