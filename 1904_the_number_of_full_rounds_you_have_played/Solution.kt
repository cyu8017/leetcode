// LeetCode 1904 - The Number Of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

class Solution {
    fun numberOfRounds(loginTime: String, logoutTime: String): Int {
        fun toMin(t: String): Int {
            val parts = t.split(":")
            return parts[0].toInt() * 60 + parts[1].toInt()
        }
        var start = toMin(loginTime)
        var end = toMin(logoutTime)
        if (end < start) end += 24 * 60
        start = (start + 14) / 15 * 15
        end = end / 15 * 15
        return maxOf(0, (end - start) / 15)
    }
}
