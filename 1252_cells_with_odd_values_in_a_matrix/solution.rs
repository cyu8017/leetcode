// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

impl Solution {
    pub fn odd_cells(m: i32, n: i32, indices: Vec<Vec<i32>>) -> i32 {
        let mut rows = vec![0; m as usize];
        let mut cols = vec![0; n as usize];
        for idx in indices {
            rows[idx[0] as usize] ^= 1;
            cols[idx[1] as usize] ^= 1;
        }
        let mut ans = 0;
        for r in 0..m as usize {
            for c in 0..n as usize {
                ans += rows[r] ^ cols[c];
            }
        }
        ans
    }
}
