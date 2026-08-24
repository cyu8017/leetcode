// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

class Solution {
    companion object {
        const val N = 31
        const val MOD = 1_000_000_007
    }
    val f = LongArray(N)
    val g = LongArray(N)
    var inited = false
    lateinit var dp: Array<Array<Array<LongArray>>>
    lateinit var nums: IntArray
    var n = 0

    fun qpow(a0: Long, k0: Long): Long {
        var a = a0
        var k = k0
        var res = 1L
        while (k > 0) {
            if ((k and 1L) != 0L) res = res * a % MOD
            a = a * a % MOD
            k = k shr 1
        }
        return res
    }

    fun initFact() {
        if (inited) return
        f[0] = 1; g[0] = 1
        for (i in 1 until N) {
            f[i] = f[i - 1] * i % MOD
            g[i] = qpow(f[i], (MOD - 2).toLong())
        }
        inited = true
    }

    fun comb(m: Int, nn: Int): Long {
        if (nn < 0 || nn > m) return 0
        return f[m] * g[nn] % MOD * g[m - nn] % MOD
    }

    fun dfs(i: Int, j: Int, kk: Int, st0: Int): Long {
        var st = st0
        var kk2 = kk
        if (kk2 < 0 || (i == n && j > 0)) return 0
        if (i == n) {
            while (st > 0) {
                kk2 -= st and 1
                st = st shr 1
            }
            return if (kk2 == 0) 1 else 0
        }
        if (dp[i][j][kk][st0] != -1L) return dp[i][j][kk][st0]
        var res = 0L
        for (t in 0..j) {
            val nt = t + st0
            val nk = kk - (nt and 1)
            val p = qpow(nums[i].toLong(), t.toLong())
            val tmp = comb(j, t) * p % MOD * dfs(i + 1, j - t, nk, nt shr 1) % MOD
            res = (res + tmp) % MOD
        }
        dp[i][j][kk][st0] = res
        return res
    }

    fun magicalSum(m: Int, k: Int, nums: IntArray): Int {
        initFact()
        this.nums = nums
        n = nums.size
        dp = Array(n + 1) { Array(m + 1) { Array(k + 1) { LongArray(N) { -1 } } } }
        return dfs(0, m, k, 0).toInt()
    }
}
