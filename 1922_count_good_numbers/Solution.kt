// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

class Solution {
    fun countGoodNumbers(n: Long): Int {
        val mod = 1_000_000_007L
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
        return (modPow(5, (n + 1) / 2) * modPow(4, n / 2) % mod).toInt()
    }
}
