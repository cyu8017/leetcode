// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

class Solution {
    private var key: BooleanArray = BooleanArray(16)
    private var s: String = ""
    private var f: Array<LongArray> = Array(16) { LongArray(10) }

    fun countGoodIntegersOnPath(l: Long, r: Long, directions: String): Long {
        key.fill(false)
        var row = 0
        var col = 0
        key[0] = true
        for (c in directions.toCharArray()) {
            if (c == 'D') row++
            else col++
            key[row * 4 + col] = true
        }
        return calc(r) - calc(l - 1)
    }

    private fun dfs(pos: Int, last: Int, lim: Boolean): Long {
        if (pos == 16) return 1
        if (!lim && f[pos][last] != -1) return f[pos][last]
        var res = 0
        var start = if (key[pos]) last else 0
        var end = if (lim) (s[pos] - '0') else 9
        for (i in start..end) {
            var nextLast = if (key[pos]) i else last
            res += dfs(pos + 1, nextLast, lim && (i == end))
        }
        if (!lim) f[pos][last] = res
        return res
    }

    private fun calc(x: Long): Long {
        if (x < 0) return 0
        var t = Long.toString(x)
        s = "0".repeat(16 - t.length) + t
        for (i in 0 until 16) { f[i].fill(-1) }
        return dfs(0, 0, true)
    }
}
