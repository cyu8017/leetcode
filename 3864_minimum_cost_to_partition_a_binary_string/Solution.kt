// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

class Solution {
    private var pre: IntArray? = null
    private var encCost: Int = 0
    private var flatCost: Int = 0

    fun minCost(s: String, encCost: Int, flatCost: Int): Long {
        var n = s.length
        this.encCost = encCost
        this.flatCost = flatCost
        pre = IntArray(n + 1)
        for (i in 1..n) { pre[i] = pre[i - 1] + (s[i - 1] - '0') }
        return dfs(0, n)
    }

    private fun dfs(l: Int, r: Int): Long {
        var x = pre[r] - pre[l]
        var res = if (x != 0) (r - l) * x * encCost else flatCost
        if ((r - l) % 2 == 0) {
            var m = (l + r) / 2
            res = minOf(res, dfs(l, m) + dfs(m, r))
        }
        return res
    }
}
