// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

impl Solution {
    pub fn largest_merge(word1: String, word2: String) -> String {
        let a = word1.as_bytes();
        let b = word2.as_bytes();
        let mut i = 0;
        let mut j = 0;
        let mut out: Vec<u8> = Vec::with_capacity(a.len() + b.len());
        while i < a.len() && j < b.len() {
            if a[i..] > b[j..] {
                out.push(a[i]);
                i += 1;
            } else {
                out.push(b[j]);
                j += 1;
            }
        }
        out.extend_from_slice(&a[i..]);
        out.extend_from_slice(&b[j..]);
        String::from_utf8(out).unwrap()
    }
}
