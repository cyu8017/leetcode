// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

import kotlin.math.abs
import kotlin.math.min

class Solution {
    fun minAbsDifference(nums: IntArray, goal: Int): Int {
        val n = nums.size
        val left = nums.copyOfRange(0, n / 2)
        val right = nums.copyOfRange(n / 2, n)

        val a = sums(left)
        val b = sums(right)
        var best = Long.MAX_VALUE
        var j = b.size - 1
        for (x in a) {
            while (j > 0 && abs(x + b[j] - goal) >= abs(x + b[j - 1] - goal)) {
                j--
            }
            best = min(best, abs(x + b[j] - goal))
        }
        return best.toInt()
    }

    private fun sums(arr: IntArray): LongArray {
        val vals = LongArray(1 shl arr.size)
        var size = 1
        for (x in arr) {
            for (i in 0 until size) {
                vals[size + i] = vals[i] + x
            }
            size *= 2
        }
        vals.sort()
        return vals
    }
}
