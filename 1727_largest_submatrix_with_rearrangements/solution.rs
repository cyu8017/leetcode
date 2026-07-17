// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

impl Solution {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let n = matrix[0].len();
        let mut heights = vec![0i32; n];
        let mut best = 0;
        for row in &matrix {
            for c in 0..n {
                heights[c] = if row[c] == 1 { heights[c] + 1 } else { 0 };
            }
            let mut sorted = heights.clone();
            sorted.sort_unstable_by(|a, b| b.cmp(a));
            for width in 1..=n {
                best = best.max(width as i32 * sorted[width - 1]);
            }
        }
        best
    }
}
