// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

class Solution {
    private lateinit var children: Array<MutableList<Int>>
    private lateinit var size: IntArray

    fun countHighestScoreNodes(parents: IntArray): Int {
var n: Int = parents.size
children = new ArrayList[n]
for (i in 0 until n) {
children[i] = mutableListOf()
}
for (i in 1 until n) {
children[parents[i]].add(i)
}
size = IntArray(n)
dfs(0)
var best: Long = 0
var ans: Int = 0
for (u in 0 until n) {
var score: Long = 1
for (v in children[u]) {
score *= size[v]
}
var up: Int = n - size[u]
if (up > 0) {
score *= up
}
if (score > best) {
best = score
ans = 1
}
else if (score == best) {
ans++
}
}
return ans
}

    private fun dfs(u: Int): Int {
size[u] = 1
for (v in children[u]) {
size[u] += dfs(v)
}
return size[u]
}
}
