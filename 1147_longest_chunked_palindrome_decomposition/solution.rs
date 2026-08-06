// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

impl Solution {
    pub fn longest_decomposition(text: String) -> i32 {
        let n = text.len();
        let bytes = text.as_bytes();
        let mut ans = 0;
        let mut i = 0;
        while i < n - i {
            let mut found = false;
            let max_len = (n - 2 * i) / 2;
            for length in 1..=max_len {
                if bytes[i..i + length] == bytes[n - i - length..n - i] {
                    ans += 2;
                    i += length;
                    found = true;
                    break;
                }
            }
            if !found {
                ans += 1;
                break;
            }
        }
        ans
    }
}
