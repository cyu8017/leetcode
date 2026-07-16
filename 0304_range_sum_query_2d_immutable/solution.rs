// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

pub struct NumMatrix {
    prefix: Vec<Vec<i32>>,
}

impl NumMatrix {
    pub fn new(matrix: Vec<Vec<i32>>) -> Self {
        let rows = matrix.len();
        let cols = if rows > 0 { matrix[0].len() } else { 0 };
        let mut prefix = vec![vec![0; cols + 1]; rows + 1];
        for row in 0..rows {
            for col in 0..cols {
                prefix[row + 1][col + 1] = matrix[row][col]
                    + prefix[row][col + 1]
                    + prefix[row + 1][col]
                    - prefix[row][col];
            }
        }
        Self { prefix }
    }

    pub fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
        let top_left = self.prefix[row1 as usize][col1 as usize];
        let top_right = self.prefix[row1 as usize][(col2 + 1) as usize];
        let bottom_left = self.prefix[(row2 + 1) as usize][col1 as usize];
        let bottom_right = self.prefix[(row2 + 1) as usize][(col2 + 1) as usize];
        bottom_right - top_right - bottom_left + top_left
    }
}
