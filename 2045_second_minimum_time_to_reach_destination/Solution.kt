// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution {
    fun secondMinimum(n: Int, edges: Array<IntArray>, time: Int, change: Int): Int {
var g: Array<MutableList<Int>> = new ArrayList[n + 1]
for (i in 0 ..n) {
g[i] = mutableListOf()
}
for (e in edges) {
g[e[0]].add(e[1])
g[e[1]].add(e[0])
}
var dist1: IntArray = IntArray(n + 1)
var dist2: IntArray = IntArray(n + 1)
dist1.fill(-1)
dist2.fill(-1)
var q: ArrayDeque<IntArray> = ArrayDeque()
q.add(intArrayOf( 1, 0 ))
dist1[1] = 0
while (!q.isEmpty()) {
var cur: IntArray = q.removeFirst()
var u: Int = cur[0]
var d: Int = cur[1]
for (v in g[u]) {
var nd: Int = d + 1
if (dist1[v] == -1) {
dist1[v] = nd
q.add(intArrayOf( v, nd ))
}
else if (dist2[v] == -1 && nd > dist1[v]) {
dist2[v] = nd
q.add(intArrayOf( v, nd ))
}
}
}
var steps: Int = dist2[n]
var ans: Int = 0
for (i in 0 until steps) {
if ((ans / change) % 2 == 1) {
ans += change - ans % change
}
ans += time
}
return ans
}
}
