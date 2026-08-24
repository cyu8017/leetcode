// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

class Solution {
    private val MOD = 1_000_000_007

    private fun modPow(a0: Long, b0: Int): Int {
        var a = a0
        var b = b0
        var res = 1L
        while (b > 0) {
            if ((b and 1) != 0) res = res * a % MOD
            a = a * a % MOD
            b = b shr 1
        }
        return res.toInt()
    }

    fun numberOfSequence(n: Int, sick: IntArray): Int {
        val fact = IntArray(n + 1)
        val invFact = IntArray(n + 1)
        fact[0] = 1
        for (i in 1..n) fact[i] = (1L * fact[i - 1] * i % MOD).toInt()
        invFact[n] = modPow(fact[n].toLong(), MOD - 2)
        for (i in n downTo 1) invFact[i - 1] = (1L * invFact[i] * i % MOD).toInt()
        val m = sick.size
        val totalEmpty = n - m
        var ans = fact[totalEmpty].toLong()
        var prev = -1
        for (s in sick) {
            val gap = s - prev - 1
            if (prev == -1) ans = ans * invFact[gap] % MOD
            else if (gap > 0) ans = ans * invFact[gap] % MOD * modPow(2, gap - 1) % MOD
            prev = s
        }
        val gap2 = n - prev - 1
        ans = ans * invFact[gap2] % MOD
        return ans.toInt()
    }
}
