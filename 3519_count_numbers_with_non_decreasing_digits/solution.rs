// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

use std::collections::HashMap;

impl Solution {
    const MOD: i32 = 1_000_000_007;

    fn to_digits(mut s: String, b: i32) -> Vec<i32> {
        if s == "0" {
            return vec![0];
        }
        let mut digs = Vec::new();
        while !(s.len() == 1 && s.as_bytes()[0] == b'0') {
            let mut rem = 0;
            let mut q = String::new();
            for c in s.bytes() {
                let cur = rem * 10 + (c - b'0') as i32;
                let d = cur / b;
                rem = cur % b;
                if !q.is_empty() || d != 0 {
                    q.push((b'0' + d as u8) as char);
                }
            }
            digs.push(rem);
            s = if q.is_empty() { "0".to_string() } else { q };
        }
        digs.reverse();
        digs
    }

    fn dec(s: String) -> String {
        let mut bytes = s.into_bytes();
        let mut i = bytes.len() as i32 - 1;
        while i >= 0 && bytes[i as usize] == b'0' {
            bytes[i as usize] = b'9';
            i -= 1;
        }
        if i < 0 {
            return "0".to_string();
        }
        bytes[i as usize] -= 1;
        let mut p = 0;
        while p + 1 < bytes.len() && bytes[p] == b'0' {
            p += 1;
        }
        String::from_utf8(bytes[p..].to_vec()).unwrap()
    }

    fn count_upto(digs: &[i32], b: i32) -> i32 {
        let m = digs.len();
        fn dfs(
            pos: usize,
            last: i32,
            tight: bool,
            m: usize,
            digs: &[i32],
            b: i32,
            memo: &mut HashMap<(usize, i32, i32), i32>,
        ) -> i32 {
            if pos == m {
                return 1;
            }
            let key = (pos, last, if tight { 1 } else { 0 });
            if let Some(&v) = memo.get(&key) {
                return v;
            }
            let up = if tight { digs[pos] } else { b - 1 };
            let mut res = 0i32;
            for d in last..=up {
                res = (res + dfs(pos + 1, d, tight && d == up, m, digs, b, memo)) % Solution::MOD;
            }
            memo.insert(key, res);
            res
        }
        let mut memo = HashMap::new();
        dfs(0, 0, true, m, digs, b, &mut memo)
    }

    pub fn count_numbers(l: String, r: String, b: i32) -> i32 {
        let rd = Self::to_digits(r, b);
        let ld = Self::to_digits(Self::dec(l), b);
        (Self::count_upto(&rd, b) - Self::count_upto(&ld, b) + Self::MOD) % Self::MOD
    }
}
