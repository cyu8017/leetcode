// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

impl Solution {
    pub fn digits_count(d: i32, low: i32, high: i32) -> i32 {
        Self::count_upto(d, high) - Self::count_upto(d, low - 1)
    }

    fn count_upto(d: i32, n: i32) -> i32 {
        if n < 0 {
            return 0;
        }
        let s = n.to_string();
        let bytes = s.as_bytes();
        let length = bytes.len();
        let mut ans = 0i32;
        for i in 0..length {
            let left: i32 = if i == 0 {
                0
            } else {
                s[..i].parse().unwrap_or(0)
            };
            let right: i32 = if i + 1 < length {
                s[i + 1..].parse().unwrap_or(0)
            } else {
                0
            };
            let digit = (bytes[i] - b'0') as i32;
            let power = 10i32.pow((length - i - 1) as u32);
            if d != 0 {
                ans += left * power;
                if digit > d {
                    ans += power;
                } else if digit == d {
                    ans += right + 1;
                }
            } else {
                if i == 0 {
                    continue;
                }
                ans += (left - 1) * power;
                if digit > 0 {
                    ans += power;
                } else {
                    ans += right + 1;
                }
            }
        }
        ans
    }
}
