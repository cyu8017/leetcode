// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/


class Solution {
    fun maxDistance(arrays: List<List<Int>>): Int {
        var minVal = arrays[0][0]
        var maxVal = arrays[0][arrays[0].size - 1]
        var best = 0
        for (i in 1 until arrays.size) {
            val cur = arrays[i]
            best = maxOf(best, kotlin.math.abs(cur[cur.size - 1] - minVal), kotlin.math.abs(maxVal - cur[0]))
            minVal = minOf(minVal, cur[0])
            maxVal = maxOf(maxVal, cur[cur.size - 1])
        }
        return best
    }
}
