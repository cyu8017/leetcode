// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

use std::collections::HashMap;

impl Solution {
    pub fn num_submatrix_sum_target(matrix: Vec<Vec<i32>>, target: i32) -> i32 {
        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut ans = 0i32;
        for left in 0..cols {
            let mut row_sum = vec![0i32; rows];
            for right in left..cols {
                for r in 0..rows {
                    row_sum[r] += matrix[r][right];
                }
                let mut prefix = 0i32;
                let mut seen: HashMap<i32, i32> = HashMap::new();
                seen.insert(0, 1);
                for &val in &row_sum {
                    prefix += val;
                    ans += seen.get(&(prefix - target)).copied().unwrap_or(0);
                    *seen.entry(prefix).or_insert(0) += 1;
                }
            }
        }
        ans
    }
}
