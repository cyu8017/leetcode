// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

class Solution {
    fun averageHeightOfBuildings(buildings: Array<IntArray>): Array<IntArray> {
var events: MutableList<IntArray> = mutableListOf()
for (b in buildings) {
events.add(intArrayOf( b[0], 1, b[2] ))
events.add(intArrayOf( b[1], -1, b[2] ))
}
events.sort(if ((a, b) -> a[0] != b[0]) Int.compare(a[0], b[0]) else Int.compare(a[1], b[1]))
var ans: MutableList<IntArray> = mutableListOf()
var count: Int = 0, sum = 0, prev = events[0][0]
for (e in events) {
if (e[0] != prev && count > 0) {
var avg: Int = sum / count
if (!ans.isEmpty() && ans[ans.size - 1][1] == prev && ans[ans.size - 1][2] == avg) {
ans[ans.size - 1][1] = e[0]
}
else {
ans.add(intArrayOf( prev, e[0], avg ))
}
}
count += e[1]
sum += e[1] * e[2]
prev = e[0]
}
return ans.toArray(IntArray(0)[])
}
}
