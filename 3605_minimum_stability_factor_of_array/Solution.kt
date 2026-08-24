// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

class Solution {
    fun minStable(nums: IntArray, maxC: Int): Int {
        val n = nums.size
        var lo = 0
        var hi = n
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (ok(nums, maxC, mid)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    fun ok(nums: IntArray, maxC: Int, x: Int): Boolean {
        val n = nums.size
        if (x >= n) return true
        var changes = 0
        var i = 0
        while (i + x < n) {
            var g = nums[i]
            for (j in i + 1..i + x) g = gcd(g, nums[j])
            if (g > 1) {
                changes++
                i += x + 1
            } else {
                i++
            }
        }
        return changes <= maxC
    }

    fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }
}
