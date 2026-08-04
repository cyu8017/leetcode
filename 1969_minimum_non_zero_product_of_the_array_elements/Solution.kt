// LeetCode 1969
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution {
    fun minNonZeroProduct(p: Int): Int {
        val mod = 1_000_000_007L
        val mx = (1L shl p) - 1
        fun modPow(base: Long, exp: Long): Long {
            var b = base % mod
            var e = exp
            var res = 1L
            while (e > 0) {
                if (e and 1L == 1L) res = res * b % mod
                b = b * b % mod
                e = e shr 1
            }
            return res
        }
        return (mx % mod * modPow(mx - 1, (1L shl (p - 1)) - 1) % mod).toInt()
    }
}
