// LeetCode 0074 - Search a 2D Matrix
// https://leetcode.com/problems/search-a-2d-matrix/

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let mut row = 0;
        let mut col = matrix[0].len() as i32 - 1;

        while row < matrix.len() as i32 && col >= 0 {
            if matrix[row as usize][col as usize] == target {
                return true;
            }
            if matrix[row as usize][col as usize] > target {
                col -= 1;
            } else {
                row += 1;
            }
        }

        false
    }
}
