// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

use std::collections::HashMap;

impl Solution {
    pub fn sort_matrix(mut grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len();
        let mut diags: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..n {
            for j in 0..n {
                diags.entry(i as i32 - j as i32).or_default().push(grid[i][j]);
            }
        }
        for (k, arr) in diags.iter_mut() {
            if *k >= 0 {
                arr.sort_by(|a, b| b.cmp(a));
            } else {
                arr.sort();
            }
        }
        let mut idx: HashMap<i32, usize> = HashMap::new();
        for i in 0..n {
            for j in 0..n {
                let k = i as i32 - j as i32;
                let pos = *idx.get(&k).unwrap_or(&0);
                grid[i][j] = diags[&k][pos];
                idx.insert(k, pos + 1);
            }
        }
        grid
    }
}
