// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

class Solution {
    private fun bitsPop(x0: Int): Int {
        var x = x0
        var c = 0
        while (x > 0) {
            c += x and 1
            x = x shr 1
        }
        return c
    }

    private lateinit var red: IntArray
    private lateinit var s: String
    private var k = 0
    private lateinit var memo: HashMap<Long, Int>
    private val mod = 1_000_000_007

    private fun key(pos: Int, tight: Int, ones: Int): Long =
        (pos.toLong() shl 32) or (tight.toLong() shl 16) or ones.toLong()

    private fun dfs(pos: Int, tight: Boolean, ones: Int): Int {
        if (pos == s.length) {
            if (ones == 0) return 0
            return if (red[ones] <= k - 1) 1 else 0
        }
        val ky = key(pos, if (tight) 1 else 0, ones)
        memo[ky]?.let { return it }
        val up = if (tight) s[pos] - '0' else 1
        var ans = 0
        for (d in 0..up) {
            val nt = tight && d == up
            ans = (ans + dfs(pos + 1, nt, ones + d)) % mod
        }
        memo[ky] = ans
        return ans
    }

    fun countKReducibleNumbers(s: String, k: Int): Int {
        this.s = s
        this.k = k
        red = IntArray(801)
        red[1] = 0
        for (i in 2..800) red[i] = 1 + red[bitsPop(i)]
        memo = HashMap()
        return dfs(0, true, 0)
    }
}
