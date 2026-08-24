// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

use std::collections::HashMap;

impl Solution {
    pub fn good_subsetof_binary_matrix(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n = grid[0].len();
        let mut first: HashMap<i32, i32> = HashMap::new();
        for (i, row) in grid.iter().enumerate() {
            let mut mask = 0i32;
            for j in 0..n {
                if row[j] == 1 {
                    mask |= 1 << j;
                }
            }
            if mask == 0 {
                return vec![i as i32];
            }
            for (&m, &idx) in &first {
                if (m & mask) == 0 {
                    return if idx < i as i32 {
                        vec![idx, i as i32]
                    } else {
                        vec![i as i32, idx]
                    };
                }
            }
            first.entry(mask).or_insert(i as i32);
        }
        vec![]
    }
}
