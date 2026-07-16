// LeetCode 0223 - Rectangle Area
// https://leetcode.com/problems/rectangle-area/

impl Solution {
    pub fn compute_area(ax1: i32, ay1: i32, ax2: i32, ay2: i32, bx1: i32, by1: i32, bx2: i32, by2: i32) -> i32 {
        let area_a = (ax2 - ax1) * (ay2 - ay1);
        let area_b = (bx2 - bx1) * (by2 - by1);
        let overlap_w = 0.max(ax2.min(bx2) - ax1.max(bx1));
        let overlap_h = 0.max(ay2.min(by2) - ay1.max(by1));
        area_a + area_b - overlap_w * overlap_h
    }
}
