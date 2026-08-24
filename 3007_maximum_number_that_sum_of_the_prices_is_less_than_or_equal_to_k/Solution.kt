// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

class Solution {
    private var num = 0L
    private var x = 0
    private lateinit var f: Array<LongArray>

    private fun dfs(pos: Int, cnt: Int, limit: Boolean): Long {
        if (pos == 0) return cnt.toLong()
        if (!limit && f[pos][cnt] != -1L) return f[pos][cnt]
        var ans = 0L
        val up = if (limit) ((num shr (pos - 1)) and 1L).toInt() else 1
        for (i in 0..up) {
            var v = cnt
            if (i == 1 && pos % x == 0) v++
            ans += dfs(pos - 1, v, limit && i == up)
        }
        if (!limit) f[pos][cnt] = ans
        return ans
    }

    fun findMaximumNumber(k: Long, x: Int): Long {
        this.x = x
        var l = 1L
        var r = 100000000000000000L // 1e17
        f = Array(65) { LongArray(65) }
        while (l < r) {
            val mid = (l + r + 1) shr 1
            num = mid
            var m = 0
            var t = num
            while (t > 0) {
                m++
                t = t shr 1
            }
            for (i in 0 until 65) {
                for (j in 0 until 65) f[i][j] = -1
            }
            if (dfs(m, 0, true) <= k) l = mid
            else r = mid - 1
        }
        return l
    }
}
