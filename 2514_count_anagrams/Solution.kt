// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

class Solution {
    private val MOD = 1_000_000_007

    private fun modPow(a0: Long, e0: Long): Long {
        var a = a0 % MOD
        var e = e0
        var res = 1L
        while (e > 0) {
            if ((e and 1L) != 0L) res = res * a % MOD
            a = a * a % MOD
            e = e shr 1
        }
        return res
    }

    fun countAnagrams(s: String): Int {
        val words = s.trim().split(Regex("\\s+")).filter { it.isNotEmpty() }
        var maxN = 0
        for (w in words) if (w.length > maxN) maxN = w.length
        val fact = LongArray(maxN + 1)
        val invFact = LongArray(maxN + 1)
        fact[0] = 1
        for (i in 1..maxN) fact[i] = fact[i - 1] * i % MOD
        invFact[maxN] = modPow(fact[maxN], (MOD - 2).toLong())
        for (i in maxN downTo 1) invFact[i - 1] = invFact[i] * i % MOD
        var ans = 1L
        for (word in words) {
            val cnt = IntArray(26)
            for (c in word) cnt[c - 'a']++
            var cur = fact[word.length]
            for (c in cnt) cur = cur * invFact[c] % MOD
            ans = ans * cur % MOD
        }
        return ans.toInt()
    }
}
