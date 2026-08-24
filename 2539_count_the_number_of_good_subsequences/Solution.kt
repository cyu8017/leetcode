// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

class Solution {
    private val MOD = 1_000_000_007
    private lateinit var fact: LongArray
    private lateinit var invFact: LongArray

    private fun modPow(a0: Long, e0: Long): Long {
        var a = a0
        var e = e0
        var res = 1L
        while (e > 0) {
            if ((e and 1L) != 0L) res = res * a % MOD
            a = a * a % MOD
            e = e shr 1
        }
        return res
    }

    private fun comb(n: Int, k: Int): Long {
        if (k < 0 || k > n) return 0
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
    }

    fun countGoodSubsequences(s: String): Int {
        val cnt = IntArray(26)
        var maxf = 0
        for (c in s) {
            cnt[c - 'a'] += 1
            if (cnt[c - 'a'] > maxf) maxf = cnt[c - 'a']
        }
        fact = LongArray(maxf + 1)
        invFact = LongArray(maxf + 1)
        fact[0] = 1
        for (i in 1..maxf) fact[i] = fact[i - 1] * i % MOD
        invFact[maxf] = modPow(fact[maxf], (MOD - 2).toLong())
        for (i in maxf downTo 1) invFact[i - 1] = invFact[i] * i % MOD
        var ans = 0L
        for (k in 1..maxf) {
            var ways = 1L
            for (i in 0 until 26) {
                if (cnt[i] >= k) ways = ways * (1 + comb(cnt[i], k)) % MOD
            }
            ans = (ans + ways - 1 + MOD) % MOD
        }
        return ans.toInt()
    }
}
