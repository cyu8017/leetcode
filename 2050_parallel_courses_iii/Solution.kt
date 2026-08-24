// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

class Solution {
    fun minimumTime(n: Int, relations: Array<IntArray>, time: IntArray): Int {
var g: Array<MutableList<Int>> = new ArrayList[n + 1]
for (i in 0 ..n) {
g[i] = mutableListOf()
}
var indeg: IntArray = IntArray(n + 1)
var dist: IntArray = IntArray(n + 1)
for (e in relations) {
g[e[0]].add(e[1])
indeg[e[1]]++
}
var q: ArrayDeque<Int> = ArrayDeque()
for (i in 1 ..n) {
dist[i] = time[i - 1]
if (indeg[i] == 0) {
q.add(i)
}
}
while (!q.isEmpty()) {
var u: Int = q.removeFirst()
for (v in g[u]) {
dist[v] = maxOf(dist[v], dist[u] + time[v - 1])
if (--indeg[v] == 0) {
q.add(v)
}
}
}
var ans: Int = 0
for (i in 1 ..n) {
ans = maxOf(ans, dist[i])
}
return ans
}
}
