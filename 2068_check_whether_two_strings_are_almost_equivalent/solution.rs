// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

impl Solution {
    pub fn check_almost_equivalent(word1: String, word2: String) -> bool {
        let mut freq = [0i32; 26];
        let a = word1.as_bytes();
        let b = word2.as_bytes();
        for i in 0..a.len() {
            freq[(a[i] - b'a') as usize] += 1;
            freq[(b[i] - b'a') as usize] -= 1;
        }
        freq.iter().all(|&v| v >= -3 && v <= 3)
    }
}
