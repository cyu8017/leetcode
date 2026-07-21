// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

impl Solution {
    pub fn min_flips(s: String) -> i32 {
        let n = s.len();
        let doubled = format!("{}{}", s, s);
        let bytes = doubled.as_bytes();
        let mut alt0 = 0i32;
        let mut alt1 = 0i32;
        for i in 0..n {
            let expect0 = if i % 2 == 0 { b'0' } else { b'1' };
            let expect1 = if i % 2 == 0 { b'1' } else { b'0' };
            if bytes[i] != expect0 {
                alt0 += 1;
            }
            if bytes[i] != expect1 {
                alt1 += 1;
            }
        }
        let mut answer = alt0.min(alt1);
        for i in 0..n {
            let expect0 = if i % 2 == 0 { b'0' } else { b'1' };
            let expect1 = if i % 2 == 0 { b'1' } else { b'0' };
            if bytes[i] != expect0 {
                alt0 -= 1;
            }
            let j = i + n;
            let expect0n = if j % 2 == 0 { b'0' } else { b'1' };
            let expect1n = if j % 2 == 0 { b'1' } else { b'0' };
            if bytes[j] != expect0n {
                alt0 += 1;
            }
            if bytes[i] != expect1 {
                alt1 -= 1;
            }
            if bytes[j] != expect1n {
                alt1 += 1;
            }
            answer = answer.min(alt0).min(alt1);
        }
        answer
    }
}
