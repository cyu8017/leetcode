#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

impl Solution {
    pub fn are_similar(mat: Vec<Vec<i32>>, k: i32) -> bool {
        let m = mat.len();
        let n = mat[0].len();
        for i in 0..m {
            let shift = if i % 2 == 0 {
                let mut s = n - (k as usize % n);
                if s == n {
                    s = 0;
                }
                s
            } else {
                k as usize % n
            };
            for j in 0..n {
                if mat[i][j] != mat[i][(j + shift) % n] {
                    return false;
                }
            }
        }
        true
    }
}
