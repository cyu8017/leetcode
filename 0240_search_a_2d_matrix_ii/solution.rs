// LeetCode 0240 - Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        if matrix.is_empty() || matrix[0].is_empty() {
            return false;
        }
        let mut row = 0;
        let mut col = matrix[0].len() as i32 - 1;
        while row < matrix.len() as i32 && col >= 0 {
            let value = matrix[row as usize][col as usize];
            if value == target {
                return true;
            }
            if value > target {
                col -= 1;
            } else {
                row += 1;
            }
        }
        false
    }
}
