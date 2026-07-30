// LeetCode 1344 - Angle Between Hands Of A Clock
// https://leetcode.com/problems/angle-between-hands-of-a-clock/

public class Solution {
    public double AngleClock(int hour, int minutes) {
        double difference = System.Math.Abs((hour % 12) * 30 + minutes * 0.5 - minutes * 6);
        return System.Math.Min(difference, 360 - difference);
    }
}
