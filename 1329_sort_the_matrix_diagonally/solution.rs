// LeetCode 1329 - Sort the Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

use std::collections::HashMap;

impl Solution {
    pub fn diagonal_sort(mut mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut diagonals: HashMap<i32, Vec<i32>> = HashMap::new();
        for (r, row) in mat.iter().enumerate() {
            for (c, &value) in row.iter().enumerate() {
                diagonals.entry(r as i32 - c as i32).or_default().push(value);
            }
        }
        for values in diagonals.values_mut() {
            values.sort_unstable_by(|a, b| b.cmp(a));
        }
        for r in 0..mat.len() {
            for c in 0..mat[0].len() {
                mat[r][c] = diagonals.get_mut(&(r as i32 - c as i32)).unwrap().pop().unwrap();
            }
        }
        mat
    }
}
