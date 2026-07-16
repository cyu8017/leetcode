// LeetCode 0054 - Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/

impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        if matrix.is_empty() {
            return Vec::new();
        }

        let mut top = 0;
        let mut bottom = matrix.len() - 1;
        let mut left = 0;
        let mut right = matrix[0].len() - 1;
        let mut result = Vec::new();

        while top <= bottom && left <= right {
            for col in left..=right {
                result.push(matrix[top][col]);
            }
            top += 1;

            for row in top..=bottom {
                result.push(matrix[row][right]);
            }
            right -= 1;

            if top <= bottom {
                for col in (left..=right).rev() {
                    result.push(matrix[bottom][col]);
                }
                bottom -= 1;
            }

            if left <= right {
                for row in (top..=bottom).rev() {
                    result.push(matrix[row][left]);
                }
                left += 1;
            }
        }

        result
    }
}
