struct Solution;
// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/

impl Solution {
    fn one(ch: u8) -> i64 {
        match ch {
            b'*' => 9,
            b'0' => 0,
            _ => 1,
        }
    }

    fn two(a: u8, b: u8) -> i64 {
        if a == b'*' && b == b'*' {
            return 15;
        }
        if a == b'*' {
            return if b <= b'6' { 2 } else { 1 };
        }
        if b == b'*' {
            return match a {
                b'1' => 9,
                b'2' => 6,
                _ => 0,
            };
        }
        let value = (a - b'0') as i32 * 10 + (b - b'0') as i32;
        if (10..=26).contains(&value) { 1 } else { 0 }
    }

    pub fn num_decodings(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let s = s.as_bytes();
        let mut prev2 = 1i64;
        let mut prev1 = Self::one(s[0]);
        for i in 1..s.len() {
            let cur = (Self::one(s[i]) * prev1 + Self::two(s[i - 1], s[i]) * prev2) % MOD;
            prev2 = prev1;
            prev1 = cur;
        }
        prev1 as i32
    }
}

fn main() {}
