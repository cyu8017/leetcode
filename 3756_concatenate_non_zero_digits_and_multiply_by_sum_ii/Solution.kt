// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum Ii
// https://leetcode.com/problems/concatenate_non_zero_digits_and_multiply_by_sum_ii/

class Solution {
    companion object {
        private const val MX = 100001
        private const val MOD = 1_000_000_007L
        private val PW = LongArray(MX)

        init {
            PW[0] = 1
            for (i in 1 until MX) PW[i] = PW[i - 1] * 10 % MOD
        }
    }

    fun sumAndMultiply(s: String, queries: Array<IntArray>): IntArray {
        val n = s.length
        val sumD = IntArray(n + 1)
        val cntN0 = IntArray(n + 1)
        val p = LongArray(n + 1)
        for (i in 1..n) {
            val d = (s[i - 1] - '0').toLong()
            sumD[i] = sumD[i - 1] + d.toInt()
            cntN0[i] = cntN0[i - 1]
            if (d > 0) {
                cntN0[i]++
                p[i] = (p[i - 1] * 10 + d) % MOD
            } else {
                p[i] = p[i - 1]
            }
        }
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val l = queries[i][0]
            val r = queries[i][1]
            val n0 = cntN0[r + 1] - cntN0[l]
            val sd = (sumD[r + 1] - sumD[l]).toLong()
            val x = (p[r + 1] - p[l] * PW[n0] % MOD + MOD) % MOD
            ans[i] = (x * sd % MOD).toInt()
        }
        return ans
    }
}
