// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

import kotlin.math.min

class Solution {
    fun findPoisonedDuration(timeSeries: IntArray, duration: Int): Int {
        if (timeSeries.isEmpty()) return 0
        var total = duration
        for (index in 1 until timeSeries.size) {
            total += min(duration, timeSeries[index] - timeSeries[index - 1])
        }
        return total
    }
}
