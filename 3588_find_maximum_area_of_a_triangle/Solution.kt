// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

class Solution {
    fun maxArea(coords: Array<IntArray>): Long {
        var ans = calc(coords)
        for (c in coords) {
            var t = c[0]
            c[0] = c[1]
            c[1] = t
        }
        ans = maxOf(ans, calc(coords))
        return if (ans > 0) ans else -1
    }

    fun calc(coords: Array<IntArray>): Long {
        var mn = 1e9
        var mx = 0
        var f = HashMap<Int, Int>()
        var g = HashMap<Int, Int>()
        for (c in coords) {
            var x = c[0]
            var y = c[1]
            mn = minOf(mn, x)
            mx = maxOf(mx, x)
            if (f.containsKey(x)) {
                f[x] = minOf(f[x], y)
                g[x] = maxOf(g[x], y)
            } else {
                f[x] = y
                g[x] = y
            }
        }
        var ans = 0
        for (e in f) {
            var x = e.key
            var y = e.value
            var d = g[x] - y
            ans = maxOf(ans, 1L * d * maxOf(mx - x, x - mn))
        }
        return ans
    }
}
