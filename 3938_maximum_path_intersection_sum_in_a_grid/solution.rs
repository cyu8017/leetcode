// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

impl Solution {
    pub fn max_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut answer = i32::MIN;
        let mut check_line = |length: usize, value: &dyn Fn(usize) -> i32| {
            let mut best_ending = value(0) + value(1);
            if best_ending > answer {
                answer = best_ending;
            }
            for i in 2..length {
                if value(i - 1) + value(i) > best_ending + value(i) {
                    best_ending = value(i - 1) + value(i);
                } else {
                    best_ending += value(i);
                }
                if best_ending > answer {
                    answer = best_ending;
                }
            }
        };
        for row in 0..rows {
            check_line(cols, &|col| grid[row][col]);
        }
        for col in 0..cols {
            check_line(rows, &|row| grid[row][col]);
        }
        for row in 1..rows.saturating_sub(1) {
            for col in 1..cols.saturating_sub(1) {
                if grid[row][col] > answer {
                    answer = grid[row][col];
                }
            }
        }
        answer
    }
}
