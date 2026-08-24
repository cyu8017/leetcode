// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

class Solution {
    fun maxFreeTime(eventTime: Int, k: Int, startTime: IntArray, endTime: IntArray): Int {
        var n = startTime.size
        var gaps = IntArray(n + 1)
        gaps[0] = startTime[0]
        for (i in 1 until n) { gaps[i] = startTime[i] - endTime[i - 1] }
        gaps[n] = eventTime - endTime[n - 1]
        var window = k + 1
        var sum = 0
        for (i in 0 until window && i < gaps.size) { sum += gaps[i] }
        var ans = sum
        for (i in window until gaps.size) {
            sum += gaps[i] - gaps[i - window]
            if (sum > ans) ans = sum
        }
        return ans
    }
}
