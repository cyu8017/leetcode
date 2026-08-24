// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

class Solution {
    fun minOperations(nums: IntArray, k: Int): Long {
        val n = nums.size
        var ans = 1L shl 62
        var i = 0
        while (i + k <= n) {
            val sub = nums.copyOfRange(i, i + k)
            sub.sort()
            val med = sub[k / 2]
            var cost = 0L
            for (x in sub) cost += kotlin.math.abs(x - med).toLong()
            if (cost < ans) ans = cost
            i++
        }
        return ans
    }
}
