// LeetCode 1344 - Angle Between Hands of a Clock
// https://leetcode.com/problems/angle-between-hands-of-a-clock/

double angleClock(int hour, int minutes) {
    double difference = (hour % 12) * 30.0 + minutes * 0.5 - minutes * 6.0;
    if (difference < 0) difference = -difference;
    return difference < 360.0 - difference ? difference : 360.0 - difference;
}
