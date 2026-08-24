// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

class Solution {
    private fun qpow(a: Long, n: Long, mod: Long): Long {
        a %= mod
        var ans = 1
        while (n > 0) {
            if ((n & 1) != 0) ans = ans * a % mod
            a = a * a % mod
            n >>= 1
        }
        return ans
    }

    fun sumOfNumbers(l: Int, r: Int, k: Int): Int {
        val MOD = 1000000007
        var n = r - l + 1
        var sum = (l + r) * n / 2 % MOD
        var part1 = qpow(n % MOD, k - 1, MOD)
        var part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD
        var inv9 = qpow(9, MOD - 2, MOD)
        var ans = sum
        ans = ans * part1 % MOD
        ans = ans * part2 % MOD
        ans = ans * inv9 % MOD
        return ans
    }
}
