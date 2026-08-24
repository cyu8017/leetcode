// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

class Solution {
    lateinit var ans: Array<IntArray>
    var `val` = 0

    fun specialGrid(n: Int): Array<IntArray> {
        val m = 1 shl n
        ans = Array(m) { IntArray(m) }
        `val` = 0
        dfs(0, m - 1, m)
        return ans
    }

    fun dfs(x: Int, y: Int, k: Int) {
        if (k == 1) {
            ans[x][y] = `val`++
            return
        }
        val h = k / 2
        dfs(x, y, h)
        dfs(x + h, y, h)
        dfs(x + h, y - h, h)
        dfs(x, y - h, h)
    }
}
