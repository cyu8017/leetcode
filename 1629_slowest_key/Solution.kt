// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

class Solution {
    fun slowestKey(releaseTimes: IntArray, keysPressed: String): Char {
        var bestDuration = releaseTimes[0]
        var bestKey = keysPressed[0]
        for (i in 1 until releaseTimes.size) {
            val duration = releaseTimes[i] - releaseTimes[i - 1]
            if (duration > bestDuration || (duration == bestDuration && keysPressed[i] > bestKey)) {
                bestDuration = duration
                bestKey = keysPressed[i]
            }
        }
        return bestKey
    }
}
