// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution {
    fun maxTwoEvents(events: Array<IntArray>): Int {
Arrays.sort(events, (a, b) -> Int.compare(a[0], b[0]))
var n: Int = events.size
var suffix: IntArray = IntArray(n + 1)
for (i in n - 1 downTo 0) {
suffix[i] = maxOf(suffix[i + 1], events[i][2])
}
var ans: Int = 0
for (i in 0 until n) {
ans = maxOf(ans, events[i][2])
var lo: Int = i + 1
var hi: Int = n
while (lo < hi) {
var mid: Int = (lo + hi) / 2
if (events[mid][0] > events[i][1]) {
hi = mid
}
else {
lo = mid + 1
}
}
if (lo < n) {
ans = maxOf(ans, events[i][2] + suffix[lo])
}
}
return ans
}
}
