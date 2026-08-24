// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

class Solution {
    fun minimumOperations(nums: IntArray, start: Int, goal: Int): Int {
if (start == goal) {
return 0
}
var vis: HashSet<Int> = HashSet()
vis.add(start)
var q: ArrayDeque<Int> = ArrayDeque()
q.add(start)
var steps: Int = 0
while (!q.isEmpty()) {
steps++
var sz: Int = q.size
while (sz-- > 0) {
var cur: Int = q.removeFirst()
for (x in nums) {
for (nxt in intArrayOf( cur + x, cur - x, cur ^ x )) {
if (nxt == goal) {
return steps
}
if (nxt >= 0 && nxt <= 1000 && vis.add(nxt)) {
q.add(nxt)
}
}
}
}
}
return -1
}
}
