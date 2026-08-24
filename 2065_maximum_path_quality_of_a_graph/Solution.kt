// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

class Solution {
    private lateinit var g: Array<MutableList<IntArray>>
    private lateinit var values: IntArray
    private var maxTime: Int = 0
    private var ans: Int = 0
    private lateinit var vis: IntArray

    fun maximalPathQuality(values: IntArray, edges: Array<IntArray>, maxTime: Int): Int {
this.values = values
this.maxTime = maxTime
var n: Int = values.length
g = new ArrayList[n]
for (i in 0 until n) {
g[i] = mutableListOf()
}
for (e in edges) {
g[e[0]].add(intArrayOf( e[1], e[2] ))
g[e[1]].add(intArrayOf( e[0], e[2] ))
}
ans = 0
vis = IntArray(n)
dfs(0, 0, 0)
return ans
}

    private fun dfs(u: Int, time: Int, quality: Int) {
if (time > maxTime) {
return
}
var first: Boolean = vis[u] == 0
if (first) {
quality += values[u]
}
vis[u]++
if (u == 0) {
ans = maxOf(ans, quality)
}
for (e in g[u]) {
dfs(e[0], time + e[1], quality)
}
vis[u]--
}
}
