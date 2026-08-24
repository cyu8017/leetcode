// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

class Solution {
    fun buttonWithLongestTime(events: Array<IntArray>): Int {
        var bestT = events[0][1]
        var bestI = events[0][0]
        for (i in 1 until events.size) {
            var t = events[i][1] - events[i - 1][1]
            if (t > bestT || (t == bestT && events[i][0] < bestI)) {
                bestT = t
                bestI = events[i][0]
            }
        }
        return bestI
    }
}
