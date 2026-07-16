// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

impl Solution {
    pub fn find_luslength(a: String, b: String) -> i32 {
        if a != b {
            return a.len().max(b.len()) as i32;
        }
        -1
    }
}
