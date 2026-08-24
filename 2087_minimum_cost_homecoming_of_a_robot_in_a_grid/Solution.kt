// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

class Solution {
    fun minCost(startPos: IntArray, homePos: IntArray, rowCosts: IntArray, colCosts: IntArray): Int {
var ans: Int = 0
var sr: Int = startPos[0]
var sc: Int = startPos[1]
var hr: Int = homePos[0]
var hc: Int = homePos[1]
if (sr < hr) {
for (r in sr + 1 ..hr) {
ans += rowCosts[r]
}
}
else {
for (r in sr - 1 downTo hr) {
ans += rowCosts[r]
}
}
if (sc < hc) {
for (c in sc + 1 ..hc) {
ans += colCosts[c]
}
}
else {
for (c in sc - 1 downTo hc) {
ans += colCosts[c]
}
}
return ans
}
}
