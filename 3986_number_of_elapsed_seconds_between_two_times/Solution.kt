// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

class Solution {
    fun toSeconds(s: String): Int {
        var h = (s[0] - '0') * 10 + (s[1] - '0')
        var m = (s[3] - '0') * 10 + (s[4] - '0')
        var sec = (s[6] - '0') * 10 + (s[7] - '0')
        return h * 3600 + m * 60 + sec
    }

    fun secondsBetweenTimes(startTime: String, endTime: String): Int {
        return toSeconds(endTime) - toSeconds(startTime)
    }
}
