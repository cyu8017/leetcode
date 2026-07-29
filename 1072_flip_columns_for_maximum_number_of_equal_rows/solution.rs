// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

use std::collections::HashMap;

impl Solution {
    pub fn max_equal_rows_after_flips(matrix: Vec<Vec<i32>>) -> i32 {
        let mut patterns: HashMap<Vec<i32>, i32> = HashMap::new();
        for row in &matrix {
            let base = row[0];
            let key: Vec<i32> = row.iter().map(|&x| x ^ base).collect();
            *patterns.entry(key).or_insert(0) += 1;
        }
        *patterns.values().max().unwrap_or(&0)
    }
}
