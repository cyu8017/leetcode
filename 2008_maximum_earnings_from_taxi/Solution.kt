// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

class Solution {
    fun maxTaxiEarnings(n: Int, rides: Array<IntArray>): Long {
Arrays.sort(rides, (a, b) -> Int.compare(a[1], b[1]))
var m: Int = rides.size
var ends: IntArray = IntArray(m)
for (i in 0 until m) {
ends[i] = rides[i][1]
}
var dp: LongArray = LongArray(m + 1)
for (i in 0 until m) {
var start: Int = rides[i][0]
var end: Int = rides[i][1]
var tip: Int = rides[i][2]
var earn: Long = end.toLong() - start + tip
var lo: Int = 0
var hi: Int = m
while (lo < hi) {
var mid: Int = (lo + hi) / 2
if (ends[mid] <= start) {
lo = mid + 1
}
else {
hi = mid
}
}
dp[i + 1] = maxOf(dp[i], earn + dp[lo])
}
return dp[m]
}
}
