// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

impl Solution {
    pub fn find_diagonal_order(mat: Vec<Vec<i32>>) -> Vec<i32> {
        if mat.is_empty() || mat[0].is_empty() {
            return Vec::new();
        }
        let rows = mat.len();
        let cols = mat[0].len();
        let mut result = Vec::with_capacity(rows * cols);
        let mut row = 0usize;
        let mut col = 0usize;
        let mut upward = true;
        for _ in 0..rows * cols {
            result.push(mat[row][col]);
            if upward {
                if col == cols - 1 {
                    row += 1;
                    upward = false;
                } else if row == 0 {
                    col += 1;
                    upward = false;
                } else {
                    row -= 1;
                    col += 1;
                }
            } else if row == rows - 1 {
                col += 1;
                upward = true;
            } else if col == 0 {
                row += 1;
                upward = true;
            } else {
                row += 1;
                col -= 1;
            }
        }
        result
    }
}
