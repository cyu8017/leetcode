// LeetCode 1344 - Angle Between Hands of a Clock
// https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution {
    fun angleClock(hour: Int, minutes: Int): Double {
        val difference = kotlin.math.abs((hour % 12) * 30.0 + minutes * 0.5 - minutes * 6.0)
        return minOf(difference, 360.0 - difference)
    }
}
