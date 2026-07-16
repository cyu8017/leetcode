// LeetCode 0059 - Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut matrix = vec![vec![0; n]; n];
        let mut top = 0;
        let mut bottom = n - 1;
        let mut left = 0;
        let mut right = n - 1;
        let mut num = 1;

        while top <= bottom && left <= right {
            for col in left..=right {
                matrix[top][col] = num;
                num += 1;
            }
            top += 1;

            for row in top..=bottom {
                matrix[row][right] = num;
                num += 1;
            }
            right -= 1;

            if top <= bottom {
                for col in (left..=right).rev() {
                    matrix[bottom][col] = num;
                    num += 1;
                }
                bottom -= 1;
            }

            if left <= right {
                for row in (top..=bottom).rev() {
                    matrix[row][left] = num;
                    num += 1;
                }
                left += 1;
            }
        }

        matrix
    }
}
