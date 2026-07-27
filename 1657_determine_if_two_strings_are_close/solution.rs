// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

impl Solution {
    pub fn close_strings(word1: String, word2: String) -> bool {
        if word1.len() != word2.len() {
            return false;
        }
        let mut a = [0i32; 26];
        let mut b = [0i32; 26];
        for c in word1.bytes() {
            a[(c - b'a') as usize] += 1;
        }
        for c in word2.bytes() {
            b[(c - b'a') as usize] += 1;
        }
        for i in 0..26 {
            if (a[i] == 0) != (b[i] == 0) {
                return false;
            }
        }
        a.sort_unstable();
        b.sort_unstable();
        a == b
    }
}
