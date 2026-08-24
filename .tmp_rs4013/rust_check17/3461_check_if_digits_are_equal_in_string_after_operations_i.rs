struct Solution;
// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

impl Solution {
    pub fn has_same_digits(s: String) -> bool {
        let mut b = s.into_bytes();
        while b.len() > 2 {
            let mut nb = vec![0; b.len() - 1];
            for i in 0..b.len() - 1 {
                nb[i] = b'0' + (b[i] - b'0' + b[i + 1] - b'0') % 10;
            }
            b = nb;
        }
        b[0] == b[1]
    }
}

fn main() {}
