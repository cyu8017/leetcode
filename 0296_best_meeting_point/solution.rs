// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

impl Solution {
    pub fn min_total_distance(grid: Vec<Vec<i32>>) -> i32 {
        let mut rows = Vec::new();
        let mut cols = Vec::new();

        for (row_index, row) in grid.iter().enumerate() {
            for (col_index, value) in row.iter().enumerate() {
                if *value == 1 {
                    rows.push(row_index as i32);
                    cols.push(col_index as i32);
                }
            }
        }

        cols.sort_unstable();
        let row_median = rows[rows.len() / 2];
        let col_median = cols[cols.len() / 2];

        let row_distance: i32 = rows.iter().map(|row| (row - row_median).abs()).sum();
        let col_distance: i32 = cols.iter().map(|col| (col - col_median).abs()).sum();
        row_distance + col_distance
    }
}
