// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

class Solution {
    private lateinit var children: Array<MutableList<Int>>
    private lateinit var nums: IntArray
    private lateinit var seen: HashSet<Int>

    fun smallestMissingValueSubtree(parents: IntArray, nums: IntArray): IntArray {
this.nums = nums
var n: Int = parents.size
children = new ArrayList[n]
for (i in 0 until n) {
children[i] = mutableListOf()
}
for (i in 1 until n) {
children[parents[i]].add(i)
}
var ans: IntArray = IntArray(n)
ans.fill(1)
var one: Int = -1
for (i in 0 until n) {
if (nums[i] == 1) {
one = i
break
}
}
if (one < 0) {
return ans
}
seen = HashSet()
var miss: Int = 1
var node: Int = one
var prev: Int = -1
while (node != -1) {
for (v in children[node]) {
if (v != prev) {
collect(v)
}
}
seen.add(nums[node])
while (seen.contains(miss)) {
miss++
}
ans[node] = miss
prev = node
node = parents[node]
}
return ans
}

    private fun collect(u: Int) {
if (seen.contains(nums[u])) {
return
}
seen.add(nums[u])
for (v in children[u]) {
collect(v)
}
}
}
