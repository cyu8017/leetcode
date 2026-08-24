// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

class Solution {
    fun maxWeight(n: Int, edges: Array<IntArray>, k: Int, t: Int): Int {
        val graph = Array(n) { ArrayList<IntArray>() }
        for (e in edges) graph[e[0]].add(intArrayOf(e[1], e[2]))
        val dp = Array(n) { Array(k + 1) { HashSet<Int>() } }
        for (u in 0 until n) dp[u][0].add(0)
        for (i in 0 until k) {
            for (u in 0 until n) {
                for (sum in dp[u][i]) {
                    for (e in graph[u]) {
                        val ns = sum + e[1]
                        if (ns < t) dp[e[0]][i + 1].add(ns)
                    }
                }
            }
        }
        var ans = -1
        for (u in 0 until n) for (sum in dp[u][k]) if (sum > ans) ans = sum
        return ans
    }
}
