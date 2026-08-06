// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

impl Solution {
    pub fn last_substring(s: String) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut i = 0usize;
        let mut j = 1usize;
        let mut k = 0usize;
        while j + k < n {
            if bytes[i + k] == bytes[j + k] {
                k += 1;
                continue;
            }
            if bytes[i + k] < bytes[j + k] {
                i += k + 1;
                if i <= j {
                    i = j;
                }
                j = i + 1;
            } else {
                j += k + 1;
            }
            k = 0;
            if j <= i {
                j = i + 1;
            }
        }
        s[i..].to_string()
    }
}
