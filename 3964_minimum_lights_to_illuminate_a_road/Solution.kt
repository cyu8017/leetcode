// LeetCode 3964 - Minimum Lights To Illuminate A Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

class Solution {
    fun minLights(lights: IntArray): Int {
        var n = lights.size
        var d = IntArray(n)
        for (i in 0 until n) {
            var v = lights[i]
            if (v > 0) {
                var l = maxOf(0, i - v)
                var r = minOf(n - 1, i + v)
                d[l]++
                if (r + 1 < n) d[r + 1]--
            }
        }
        var s = 0
        var cnt = 0
        var ans = 0
        for (x in d) {
            s += x
            if (s == 0) cnt++
            else {
                ans += (cnt + 2) / 3
                cnt = 0
            }
        }
        ans += (cnt + 2) / 3
        return ans
    }
}
