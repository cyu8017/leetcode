// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution {
    fun maxDistance(colors: IntArray): Int {
var n: Int = colors.size
var ans: Int = 0
for (i in 0 until n) {
if (colors[i] != colors[0]) {
ans = maxOf(ans, i)
}
if (colors[i] != colors[n - 1]) {
ans = maxOf(ans, n - 1 - i)
}
}
return ans
}
}
