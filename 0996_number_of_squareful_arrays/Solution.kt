// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

class Solution {
    private var ans: Int = 0
    private lateinit var count: HashMap<Int, Int>
    private lateinit var graph: HashMap<Int, MutableList<Int>>

    fun numSquarefulPerms(nums: IntArray): Int {
count = HashMap()
for (x in nums) {
count.merge(x, 1, { a, b -> a + b })
}
graph = HashMap()
for (a in count.keySet()) {
graph.put(a, mutableListOf())
}
for (a in count.keySet()) {
for (b in count.keySet()) {
var s: Long = a.toLong() + b
var r: Long = Math.round(kotlin.math.sqrt(s))
if (r * r == s) {
graph[a].add(b)
}
}
}
ans = 0
for (x in ArrayList(count.keySet())) {
count.put(x, count[x] - 1)
dfs(x, nums.size - 1)
count.put(x, count[x] + 1)
}
return ans
}

    private fun dfs(x: Int, remain: Int) {
if (remain == 0) {
ans++
return
}
for (y in graph[x]) {
if (count[y] > 0) {
count.put(y, count[y] - 1)
dfs(y, remain - 1)
count.put(y, count[y] + 1)
}
}
}
}
