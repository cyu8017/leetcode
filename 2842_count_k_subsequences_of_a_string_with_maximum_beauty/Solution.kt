// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

class Solution {
    private val MOD = 1_000_000_007

    fun countKSubsequencesWithMaxBeauty(s: String, k: Int): Int {
        val freq = IntArray(26)
        for (ch in s) freq[ch - 'a']++
        val vals = ArrayList<Int>()
        for (f in freq) if (f > 0) vals.add(f)
        if (vals.size < k) return 0
        vals.sortDescending()
        val threshold = vals[k - 1]
        var need = 0
        var avail = 0
        var prod = 1L
        for (v in vals) {
            if (v > threshold) {
                prod = prod * v % MOD
                need++
            } else if (v == threshold) {
                avail++
            }
        }
        val remain = k - need
        prod = prod * comb(avail, remain) % MOD
        repeat(remain) { prod = prod * threshold % MOD }
        return prod.toInt()
    }

    private fun modPow(a0: Long, b0: Long): Long {
        var a = a0 % MOD
        var b = b0
        var res = 1L
        while (b > 0) {
            if ((b and 1L) != 0L) res = res * a % MOD
            a = a * a % MOD
            b = b shr 1
        }
        return res
    }

    private fun comb(n: Int, r: Int): Long {
        if (r < 0 || r > n) return 0
        var num = 1L
        var den = 1L
        for (i in 0 until r) {
            num = num * (n - i) % MOD
            den = den * (i + 1) % MOD
        }
        return num * modPow(den, (MOD - 2).toLong()) % MOD
    }
}
