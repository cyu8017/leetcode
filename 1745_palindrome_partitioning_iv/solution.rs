// LeetCode 1745 - Palindrome Partitioning IV
// https://leetcode.com/problems/palindrome-partitioning-iv/

impl Solution {
    pub fn check_partitioning(s: String) -> bool {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut pal = vec![vec![false; n]; n];
        for i in (0..n).rev() {
            for j in i..n {
                pal[i][j] = bytes[i] == bytes[j] && (j - i < 2 || pal[i + 1][j - 1]);
            }
        }
        for i in 0..n.saturating_sub(2) {
            for j in i + 1..n - 1 {
                if pal[0][i] && pal[i + 1][j] && pal[j + 1][n - 1] {
                    return true;
                }
            }
        }
        false
    }
}
