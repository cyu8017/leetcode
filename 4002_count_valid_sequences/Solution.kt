// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/

class Solution {
    private val MX: Int = 500001
    private val MOD: Long = 1000000007L
    private val f: LongArray = LongArray(MX)
    private val g: LongArray = LongArray(MX)
    private var inited: Boolean = false

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

    private fun ensureInit() {
        if (inited) return
        inited = true
        f[0] = 1
        g[0] = 1
        for (i in 1 until MX) {
            f[i] = f[i - 1] * i % MOD
            g[i] = modPow(f[i], MOD - 2)
        }
    }

    private fun comb(n: Int, k: Int): Long {
        if (k < 0 || k > n) return 0
        return f[n] * g[k] % MOD * g[n - k] % MOD
    }

    fun countValidSequences(n: Int, k: Int): Int {
        ensureInit()
        var ans = comb(n - 1, k - 1)
        if ((n + k) % 2 == 0) {
            ans = (ans - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD
        }
        return ans.toInt()
    }
}
