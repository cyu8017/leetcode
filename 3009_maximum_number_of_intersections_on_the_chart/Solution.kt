// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

import java.util.TreeMap

class Solution {
    fun maxIntersectionCount(y: IntArray): Int {
        val n = y.size
        val line = TreeMap<Int, Int>()
        for (i in 1 until n) {
            val start = 2 * y[i - 1]
            var end = 2 * y[i]
            if (i != n - 1) {
                if (y[i] > y[i - 1]) end-- else end++
            }
            var a = start; var b = end
            if (a > b) { val t = a; a = b; b = t }
            line[a] = line.getOrDefault(a, 0) + 1
            line[b + 1] = line.getOrDefault(b + 1, 0) - 1
        }
        var ans = 0; var cur = 0
        for (v in line.values) { cur += v; if (cur > ans) ans = cur }
        return ans
    }
}
