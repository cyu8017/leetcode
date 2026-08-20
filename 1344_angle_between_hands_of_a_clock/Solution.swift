// LeetCode 1344 - Angle Between Hands of a Clock
// https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution {
    func angleClock(_ hour: Int, _ minutes: Int) -> Double {
        let difference = abs(Double(hour % 12) * 30 + Double(minutes) * 0.5 - Double(minutes) * 6)
        return min(difference, 360 - difference)
    }
}
