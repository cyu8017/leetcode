// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        let mut freq = [0i32; 26];
        for c in s.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        for c in t.bytes() {
            freq[(c - b'a') as usize] -= 1;
        }
        freq.iter().map(|&v| v.abs()).sum()
    }
}
