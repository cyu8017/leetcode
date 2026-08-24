// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

impl Solution {
    pub fn matrix_reshape(mat: Vec<Vec<i32>>, r: i32, c: i32) -> Vec<Vec<i32>> {
        let rows = mat.len() as i32;
        let cols = mat[0].len() as i32;
        if rows * cols != r * c {
            return mat;
        }
        let mut result = vec![vec![0; c as usize]; r as usize];
        let mut index = 0;
        for i in 0..r as usize {
            for j in 0..c as usize {
                result[i][j] = mat[index / cols as usize][index % cols as usize];
                index += 1;
            }
        }
        result
    }
}
