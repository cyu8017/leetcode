// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

impl Solution {
    pub fn to_hexspeak(num: String) -> String {
        let mut value: i64 = num.parse().unwrap();
        let digits = b"0123456789ABCDEF";
        if value == 0 {
            return "O".to_string();
        }
        let mut out = Vec::new();
        while value > 0 {
            let rem = (value % 16) as usize;
            if (2..=9).contains(&rem) {
                return "ERROR".to_string();
            }
            out.push(digits[rem]);
            value /= 16;
        }
        out.reverse();
        for b in &mut out {
            if *b == b'0' {
                *b = b'O';
            } else if *b == b'1' {
                *b = b'I';
            }
        }
        String::from_utf8(out).unwrap()
    }
}
