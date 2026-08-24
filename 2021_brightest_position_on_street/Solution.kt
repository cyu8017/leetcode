// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

class Solution {
    fun brightestPosition(lights: Array<IntArray>): Int {
var events: MutableList<IntArray> = mutableListOf()
for (light in lights) {
var pos: Int = light[0]
var r: Int = light[1]
events.add(intArrayOf( pos - r, 1 ))
events.add(intArrayOf( pos + r + 1, -1 ))
}
events.sort(if ((a, b) -> a[0] != b[0]) Int.compare(a[0], b[0]) else Int.compare(b[1], a[1]))
var best: Int = 0
var cur: Int = 0
var ans: Int = 0
for (e in events) {
cur += e[1]
if (cur > best) {
best = cur
ans = e[0]
}
}
return ans
}
}
