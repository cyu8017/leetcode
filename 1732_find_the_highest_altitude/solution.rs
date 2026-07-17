// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut altitude = 0;
        let mut best = 0;
        for change in gain {
            altitude += change;
            best = best.max(altitude);
        }
        best
    }
}
