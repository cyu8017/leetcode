// LeetCode 1351 - Count Negative Numbers in a Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        grid.iter()
            .map(|row| {
                let n = row.len();
                let i = row.iter().position(|&x| x < 0).unwrap_or(n);
                (n - i) as i32
            })
            .sum()
    }
}
