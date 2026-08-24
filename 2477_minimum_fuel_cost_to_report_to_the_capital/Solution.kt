// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private var ans = 0L
    private var seats = 0

    private fun dfs(u: Int, p: Int): Int {
        var people = 1
        for (v in g[u]) if (v != p) people += dfs(v, u)
        if (u != 0) ans += (people + seats - 1) / seats
        return people
    }

    fun minimumFuelCost(roads: Array<IntArray>, seats: Int): Long {
        this.seats = seats
        val n = roads.size + 1
        g = Array(n) { ArrayList() }
        for (r in roads) {
            g[r[0]].add(r[1])
            g[r[1]].add(r[0])
        }
        ans = 0
        dfs(0, -1)
        return ans
    }
}
