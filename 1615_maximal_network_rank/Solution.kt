// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

class Solution {
    fun maximalNetworkRank(n: Int, roads: Array<IntArray>): Int {
        val degree = IntArray(n)
        val edges = HashSet<Pair<Int, Int>>()
        for (r in roads) {
            val a = r[0]
            val b = r[1]
            degree[a]++
            degree[b]++
            edges.add(minOf(a, b) to maxOf(a, b))
        }
        var ans = 0
        for (a in 0 until n) {
            for (b in a + 1 until n) {
                var rank = degree[a] + degree[b]
                if ((a to b) in edges) rank--
                ans = maxOf(ans, rank)
            }
        }
        return ans
    }
}
