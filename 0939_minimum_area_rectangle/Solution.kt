// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

class Solution {
    fun minAreaRect(points: Array<IntArray>): Int {
        val byX = java.util.TreeMap<Int, MutableList<Int>>()
        for (p in points) {
            byX.getOrPut(p[0]) { mutableListOf() }.add(p[1])
        }
        val last = HashMap<String, Int>()
        var ans = Long.MAX_VALUE
        for ((x, ys) in byX) {
            ys.sort()
            for (i in ys.indices) {
                for (j in i + 1 until ys.size) {
                    val key = "${ys[i]}#${ys[j]}"
                    if (last.containsKey(key)) {
                        ans = minOf(ans, kotlin.math.abs(x - last[key]!!).toLong() * (ys[j] - ys[i]))
                    }
                    last[key] = x
                }
            }
        }
        return if (ans == Long.MAX_VALUE) 0 else ans.toInt()
    }
}
