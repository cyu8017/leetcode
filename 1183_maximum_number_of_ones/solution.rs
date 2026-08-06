// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

impl Solution {
    pub fn maximum_number_of_ones(width: i32, height: i32, side_length: i32, max_ones: i32) -> i32 {
        let mut counts = Vec::new();
        for r in 0..side_length {
            for c in 0..side_length {
                let rows = (height - r + side_length - 1) / side_length;
                let cols = (width - c + side_length - 1) / side_length;
                counts.push(rows * cols);
            }
        }
        counts.sort_unstable_by(|a, b| b.cmp(a));
        counts.into_iter().take(max_ones as usize).sum()
    }
}
