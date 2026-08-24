// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

class Solution {
    fun maxPointsInsideSquare(points: Array<IntArray>, s: String): Int {
        var g = TreeMap<Int, MutableList<Int>>()
        for (i in 0 until points.size) {
            var key = maxOf(maxOf(points[i][0], -points[i][0]), maxOf(points[i][1], -points[i][1]))
            g.computeIfAbsent(key, k -> ArrayList()).add(i)
        }
        var vis = BooleanArray(26)
        var ans = 0
        for (e in g) {
            for (i in e.value) {
                var j = s[i] - 'a'
                if (vis[j]) return ans
                vis[j] = true
            }
            ans += e.value.size
        }
        return ans
    }
}
