// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

impl Solution {
    pub fn longest_subsequence(s: String, k: i32) -> i32 {
        let k = k as i64;
        let bytes = s.as_bytes();
        let zeros = bytes.iter().filter(|&&c| c == b'0').count() as i32;
        let mut val = 0i64;
        let mut ones = 0i32;
        let mut pow = 1i64;
        for i in (0..bytes.len()).rev() {
            if bytes[i] == b'1' {
                if pow <= k && val + pow <= k {
                    val += pow;
                    ones += 1;
                }
            }
            if pow <= k {
                if pow > (1i64 << 60) {
                    pow = k + 1;
                } else {
                    pow <<= 1;
                }
            }
        }
        zeros + ones
    }
}
