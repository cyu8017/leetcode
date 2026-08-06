// LeetCode 1401 - Circle and Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/

impl Solution {
    pub fn check_overlap(
        radius: i32,
        x_center: i32,
        y_center: i32,
        x1: i32,
        y1: i32,
        x2: i32,
        y2: i32,
    ) -> bool {
        let x = x_center.max(x1).min(x2);
        let y = y_center.max(y1).min(y2);
        (x - x_center).pow(2) + (y - y_center).pow(2) <= radius.pow(2)
    }
}
