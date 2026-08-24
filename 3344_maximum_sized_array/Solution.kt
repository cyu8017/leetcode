// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

class Solution {
    private fun ok(n: Long, s: Long): Boolean {
        var sum = 0
        for (i in 0 until n) {
            for (j in 0 until n) {
                var ij = i or j
                sum += ij * (n - 1) * n / 2
                if (sum > s) return false
            }
        }
        return sum <= s
    }

    fun maxSizedArray(s: Long): Int {
        var lo = 1
        var hi = 2000
        while (lo < hi) {
            var mid = (lo + hi + 1) / 2
            if (ok(mid, s)) lo = mid
            else hi = mid - 1
        }
        return lo
    }
}
