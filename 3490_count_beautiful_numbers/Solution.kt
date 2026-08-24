// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

class Solution {
    private var s: String? = null

    private fun countBeautiful(n: Int): Int {
        if (n <= 0) return 0
        s = n.toString()
        return dfs(0, true, 0, 1, false)
    }

    private fun dfs(pos: Int, tight: Boolean, sum: Int, prod: Int, started: Boolean): Int {
        if (pos == s.length) {
            if (!started) return 0
            return if ((sum > 0 && prod % sum == 0)) 1 else 0
        }
        var up = if (tight) (s[pos] - '0') else 9
        var ans = 0
        for (d in 0 .. up) {
            var nt = tight && d == up
            if (!started && d == 0) ans += dfs(pos + 1, nt, 0, 1, false)
            else {
                var ns = sum + d
                var np = if (!started) d else prod * d
                ans += dfs(pos + 1, nt, ns, np, true)
            }
        }
        return ans
    }

    fun beautifulNumbers(l: Int, r: Int): Int {
        return countBeautiful(r) - countBeautiful(l - 1)
    }
}
