// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

impl Solution {
    pub fn max_width_of_vertical_area(points: Vec<Vec<i32>>) -> i32 {
        let mut xs: Vec<i32> = points.into_iter().map(|p| p[0]).collect();
        xs.sort_unstable();
        xs.windows(2).map(|w| w[1] - w[0]).max().unwrap_or(0)
    }
}
