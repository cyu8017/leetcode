// LeetCode 1428 - Leftmost Column with at Least a One
// https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * struct BinaryMatrix;
 * impl BinaryMatrix {
 *     fn get(&self, row: i32, col: i32) -> i32;
 *     fn dimensions(&self) -> Vec<i32>;
 * };
 */

impl Solution {
    pub fn left_most_column_with_one(binary_matrix: &BinaryMatrix) -> i32 {
        let dims = binary_matrix.dimensions();
        let (rows, cols) = (dims[0], dims[1]);
        let mut row = 0;
        let mut col = cols - 1;
        let mut answer = -1;
        while row < rows && col >= 0 {
            if binary_matrix.get(row, col) == 1 {
                answer = col;
                col -= 1;
            } else {
                row += 1;
            }
        }
        answer
    }
}
