// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution {
    fun minimizedMaximum(n: Int, quantities: IntArray): Int {
var lo: Int = 1
var hi: Int = 0
for (q in quantities) {
hi = maxOf(hi, q)
}
while (lo < hi) {
var mid: Int = (lo + hi) / 2
if (can(n, quantities, mid)) {
hi = mid
}
else {
lo = mid + 1
}
}
return lo
}

    private fun can(n: Int, quantities: IntArray, x: Int): Boolean {
var need: Int = 0
for (q in quantities) {
need += (q + x - 1) / x
if (need > n) {
return false
}
}
return true
}
}
