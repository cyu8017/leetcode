// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

class Solution {
    fun makeStringSorted(s: String): Int {
        val mod = 1_000_000_007L
        val n = s.length
        val fact = LongArray(n + 1)
        fact[0] = 1
        for (i in 1..n) fact[i] = fact[i - 1] * i % mod

        val invFact = LongArray(n + 1)
        invFact[n] = modPow(fact[n], mod - 2, mod)
        for (i in n - 1 downTo 0) invFact[i] = invFact[i + 1] * (i + 1) % mod

        val freq = IntArray(26)
        for (ch in s) freq[ch - 'a']++

        var ans = 0L
        for (i in s.indices) {
            val c = s[i] - 'a'
            for (smaller in 0 until c) {
                if (freq[smaller] == 0) continue
                freq[smaller]--
                var ways = fact[n - i - 1]
                for (count in freq) ways = ways * invFact[count] % mod
                ans = (ans + ways) % mod
                freq[smaller]++
            }
            freq[c]--
        }
        return ans.toInt()
    }

    private fun modPow(base: Long, exp: Long, mod: Long): Long {
        var b = base % mod
        var e = exp
        var result = 1L
        while (e > 0) {
            if (e and 1L == 1L) result = result * b % mod
            b = b * b % mod
            e = e shr 1
        }
        return result
    }
}
