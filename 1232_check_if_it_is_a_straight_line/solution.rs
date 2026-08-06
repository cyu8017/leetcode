// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

impl Solution {
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
        let x0 = coordinates[0][0];
        let y0 = coordinates[0][1];
        let dx = coordinates[1][0] - x0;
        let dy = coordinates[1][1] - y0;
        for p in &coordinates[2..] {
            if (p[0] - x0) * dy != (p[1] - y0) * dx {
                return false;
            }
        }
        true
    }
}
