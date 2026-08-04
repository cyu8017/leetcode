// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

class Solution {
    fun longestWPI(hours: IntArray): Int {
        var score = 0
        val firstSeen = mutableMapOf(0 to -1)
        var ans = 0
        for (i in hours.indices) {
            score += if (hours[i] > 8) 1 else -1
            if (score > 0) {
                ans = i + 1
            } else if (score - 1 in firstSeen) {
                ans = maxOf(ans, i - firstSeen[score - 1]!!)
            }
            firstSeen.putIfAbsent(score, i)
        }
        return ans
    }
}
