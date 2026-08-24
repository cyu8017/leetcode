// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

impl Solution {
    pub fn number_of_substrings(s: String) -> i64 {
        let mut freq = [0i64; 26];
        let mut ans = 0i64;
        for c in s.bytes() {
            let i = (c - b'a') as usize;
            freq[i] += 1;
            ans += freq[i];
        }
        ans
    }
}
