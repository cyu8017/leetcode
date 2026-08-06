// LeetCode 1380 - Lucky Numbers in a Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

use std::collections::HashSet;

impl Solution {
    pub fn lucky_numbers(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mins: HashSet<i32> = matrix.iter().map(|r| *r.iter().min().unwrap()).collect();
        let cols = matrix[0].len();
        let mut maxs = HashSet::new();
        for c in 0..cols {
            maxs.insert(matrix.iter().map(|r| r[c]).max().unwrap());
        }
        mins.intersection(&maxs).copied().collect()
    }
}
