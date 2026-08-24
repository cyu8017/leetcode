struct Solution;
// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

impl Solution {
    fn to_binary(mut v: i32) -> String {
        if v == 0 {
            return "0".to_string();
        }
        let mut s = String::new();
        while v > 0 {
            s.insert(0, char::from(b'0' + (v & 1) as u8));
            v >>= 1;
        }
        s
    }

    pub fn convert_date_to_binary(date: String) -> String {
        let parts: Vec<i32> = date.split('-').map(|p| p.parse().unwrap()).collect();
        format!(
            "{}-{}-{}",
            Self::to_binary(parts[0]),
            Self::to_binary(parts[1]),
            Self::to_binary(parts[2])
        )
    }
}

fn main() {}
