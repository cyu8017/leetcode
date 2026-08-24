// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

impl Solution {
    pub fn minimum_flips(n: i32) -> i32 {
        let mut x = n as i64;
        let mut s = String::new();
        if x == 0 {
            s = "0".to_string();
        } else {
            while x > 0 {
                s.push(char::from(b'0' + (x & 1) as u8));
                x >>= 1;
            }
            let mut bytes = s.into_bytes();
            bytes.reverse();
            s = String::from_utf8(bytes).unwrap();
        }
        let m = s.len();
        let bytes = s.as_bytes();
        let mut cnt = 0;
        for i in 0..m / 2 {
            if bytes[i] != bytes[m - i - 1] {
                cnt += 1;
            }
        }
        cnt * 2
    }
}
