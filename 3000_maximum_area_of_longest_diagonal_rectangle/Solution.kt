// LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
// https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

class Solution {
    fun areaOfMaxDiagonal(dimensions: Array<IntArray>): Int {
        var ans = 0
        var mx = 0
        for (var d : dimensions) {
            var l = d[0]
            var w = d[1]
            var t = l * l + w * w
            if (mx < t) {
                mx = t
                ans = l * w
            } else if (mx == t) {
                ans = maxOf(ans, l * w)
            }
        }
        return ans
    }
}
