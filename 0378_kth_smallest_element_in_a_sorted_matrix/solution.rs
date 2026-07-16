// LeetCode 0378 - Kth Smallest Element in a Sorted Matrix
// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

impl Solution {
    pub fn kth_smallest(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        let rows = matrix.len();
        let mut left = matrix[0][0];
        let mut right = matrix[rows - 1][rows - 1];

        while left < right {
            let mid = left + (right - left) / 2;
            let mut count = 0;
            let mut column = rows as i32 - 1;

            for row in 0..rows {
                while column >= 0 && matrix[row][column as usize] > mid {
                    column -= 1;
                }
                count += column + 1;
            }

            if count < k {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        left
    }
}
