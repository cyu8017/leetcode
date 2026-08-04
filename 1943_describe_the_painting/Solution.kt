// LeetCode 1943
// https://leetcode.com/problems/describe-the-painting/

class Solution {
    fun splitPainting(segments: Array<IntArray>): List<List<Long>> {
        val diff = sortedMapOf<Int, Long>()
        for (seg in segments) {
            diff[seg[0]] = diff.getOrDefault(seg[0], 0L) + seg[2]
            diff[seg[1]] = diff.getOrDefault(seg[1], 0L) - seg[2]
        }
        val points = diff.keys.toList()
        val ans = mutableListOf<List<Long>>()
        var cur = 0L
        for (i in 0 until points.size - 1) {
            cur += diff[points[i]]!!
            if (cur != 0L) ans.add(listOf(points[i].toLong(), points[i + 1].toLong(), cur))
        }
        return ans
    }
}
