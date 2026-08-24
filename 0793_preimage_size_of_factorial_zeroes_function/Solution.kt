// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

class Solution {
    fun preimageSizeFZF(k: Int): Int {
        return (firstGe(k + 1) - firstGe(k))
    }

    private fun zeros(n: Long): Long {
        var n = n
        var z = 0
        while (n > 0) {
            n /= 5
            z += n
        }
        return z
    }

    private fun firstGe(target: Long): Long {
        var lo = 0
        var hi = 5L * target + 5
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (zeros(mid) >= target) hi = mid
            else lo = mid + 1
        }
        return lo
    }
}
