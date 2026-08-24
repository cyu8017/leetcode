// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

class Solution {
    private lateinit var num: String
    private lateinit var f: Array<IntArray>

    private fun reset() {
        f = Array(num.length) { IntArray(1 shl 10) { -1 } }
    }

    private fun dfs(pos: Int, mask: Int, limit: Boolean): Int {
        if (pos >= num.length) return if (mask != 0) 1 else 0
        if (!limit && f[pos][mask] != -1) return f[pos][mask]
        val up = if (limit) num[pos] - '0' else 9
        var ans = 0
        for (i in 0..up) {
            if (((mask shr i) and 1) != 0) continue
            var nxt = mask or (1 shl i)
            if (mask == 0 && i == 0) nxt = 0
            ans += dfs(pos + 1, nxt, limit && i == up)
        }
        if (!limit) f[pos][mask] = ans
        return ans
    }

    fun numberCount(a: Int, b: Int): Int {
        num = b.toString()
        reset()
        val y = dfs(0, 0, true)
        num = (a - 1).toString()
        reset()
        val x = dfs(0, 0, true)
        return y - x
    }
}
