// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

impl Solution {
    pub fn kth_largest_value(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut pref = vec![vec![0i32; cols + 1]; rows + 1];
        let mut values = Vec::with_capacity(rows * cols);
        for r in 1..=rows {
            for c in 1..=cols {
                pref[r][c] = pref[r - 1][c] ^ pref[r][c - 1] ^ pref[r - 1][c - 1] ^ matrix[r - 1][c - 1];
                values.push(pref[r][c]);
            }
        }
        values.sort_unstable_by(|a, b| b.cmp(a));
        values[(k - 1) as usize]
    }
}
