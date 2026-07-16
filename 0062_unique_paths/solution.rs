// LeetCode 0062 - Unique Paths
// https://leetcode.com/problems/unique-paths/

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let m = m as usize;
        let n = n as usize;
        let mut row = vec![1; n];

        for _ in 1..m {
            for col in 1..n {
                row[col] += row[col - 1];
            }
        }

        row[n - 1]
    }
}
