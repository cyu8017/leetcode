// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

class Solution {
    fun waysToSplit(nums: IntArray): Int {
        val mod = 1_000_000_007L
        val n = nums.size
        val prefix = LongArray(n)
        var total = 0L
        for (i in nums.indices) {
            total += nums[i]
            prefix[i] = total
        }

        fun lowerBound(target: Long, start: Int, end: Int): Int {
            var lo = start
            var hi = end
            while (lo < hi) {
                val mid = (lo + hi) ushr 1
                if (prefix[mid] < target) {
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            return lo
        }

        fun upperBound(target: Long, start: Int, end: Int): Int {
            var lo = start
            var hi = end
            while (lo < hi) {
                val mid = (lo + hi) ushr 1
                if (prefix[mid] <= target) {
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            return lo
        }

        var ans = 0L
        for (i in 0 until n - 2) {
            val left = prefix[i]
            val lo = lowerBound(2 * left, i + 1, n - 1)
            val hi = upperBound((total + left) / 2, lo, n - 1)
            ans = (ans + hi - lo) % mod
        }
        return ans.toInt()
    }
}
