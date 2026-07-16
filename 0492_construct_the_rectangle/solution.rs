// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

impl Solution {
    pub fn construct_rectangle(area: i32) -> Vec<i32> {
        let limit = (area as f64).sqrt() as i32;
        for width in (1..=limit).rev() {
            if area % width == 0 {
                return vec![area / width, width];
            }
        }
        vec![area, 1]
    }
}
