// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

class Solution {
    fun findMinDifference(timePoints: List<String>): Int {
        val minutes = timePoints.map { time ->
            val parts = time.split(":")
            parts[0].toInt() * 60 + parts[1].toInt()
        }.sorted()

        var best = minutes.last() - minutes.first()
        for (i in 1 until minutes.size) {
            best = minOf(best, minutes[i] - minutes[i - 1])
        }
        return minOf(best, 24 * 60 - minutes.last() + minutes.first())
    }
}
