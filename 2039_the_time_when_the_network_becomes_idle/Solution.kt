// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

class Solution {
    fun networkBecomesIdle(edges: Array<IntArray>, patience: IntArray): Int {
var n: Int = patience.size
var g: Array<MutableList<Int>> = new ArrayList[n]
for (i in 0 until n) {
g[i] = mutableListOf()
}
for (e in edges) {
g[e[0]].add(e[1])
g[e[1]].add(e[0])
}
var dist: IntArray = IntArray(n)
dist.fill(-1)
var q: ArrayDeque<Int> = ArrayDeque()
q.add(0)
dist[0] = 0
while (!q.isEmpty()) {
var u: Int = q.removeFirst()
for (v in g[u]) {
if (dist[v] == -1) {
dist[v] = dist[u] + 1
q.add(v)
}
}
}
var ans: Int = 0
for (i in 1 until n) {
var round: Int = dist[i] * 2
var lastSend: Int = (round - 1) / patience[i] * patience[i]
ans = maxOf(ans, lastSend + round)
}
return ans + 1
}
}
