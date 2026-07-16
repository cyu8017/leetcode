// LeetCode 0392 - Is Subsequence
// https://leetcode.com/problems/is-subsequence/

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let s_bytes = s.as_bytes();
        let mut index = 0;

        for ch in t.bytes() {
            if index < s_bytes.len() && s_bytes[index] == ch {
                index += 1;
            }
        }

        index == s_bytes.len()
    }
}
