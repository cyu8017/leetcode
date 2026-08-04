// LeetCode 1344 - Angle Between Hands Of A Clock
// https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution {
    public double angleClock(int hour, int minutes) {
        double difference = Math.abs((hour % 12) * 30 + minutes * 0.5 - minutes * 6);
        return Math.min(difference, 360 - difference);
    }
}
