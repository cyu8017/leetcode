struct Solution;
// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

impl Solution {
    pub fn count_substrings(s: String) -> i64 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut ans = 0i64;
        for r in 0..n {
            let last = (bytes[r] - b'0') as i32;
            if last == 0 {
                continue;
            }
            let mut modulus = 0;
            let mut p = 1 % last;
            for l in (0..=r).rev() {
                modulus = (modulus + (bytes[l] - b'0') as i32 * p) % last;
                p = (p * 10) % last;
                if modulus == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}

fn main() {}
