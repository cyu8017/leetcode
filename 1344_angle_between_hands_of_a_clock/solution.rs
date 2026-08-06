// LeetCode 1344 - Angle Between Hands of a Clock
// https://leetcode.com/problems/angle-between-hands-of-a-clock/

impl Solution {
    pub fn angle_clock(hour: i32, minutes: i32) -> f64 {
        let difference = ((hour % 12) as f64 * 30.0 + minutes as f64 * 0.5 - minutes as f64 * 6.0).abs();
        difference.min(360.0 - difference)
    }
}
