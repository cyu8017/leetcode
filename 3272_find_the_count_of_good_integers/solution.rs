// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

use std::collections::HashSet;

impl Solution {
    fn itoa(mut x: i32) -> String {
        if x == 0 {
            return "0".to_string();
        }
        let mut b = String::new();
        while x > 0 {
            b.insert(0, char::from(b'0' + (x % 10) as u8));
            x /= 10;
        }
        b
    }

    fn atoi_str(s: &str) -> i64 {
        let mut v = 0i64;
        for c in s.bytes() {
            v = v * 10 + (c - b'0') as i64;
        }
        v
    }

    pub fn count_good_integers(n: i32, k: i32) -> i64 {
        let half = (n + 1) / 2;
        let mut start = 1;
        for _ in 1..half {
            start *= 10;
        }
        let end = start * 10;
        let mut seen = HashSet::new();
        let mut ans = 0i64;
        let mut fact = vec![1i64; (n + 1) as usize];
        for i in 1..=n as usize {
            fact[i] = fact[i - 1] * i as i64;
        }
        for h in start..end {
            let s = Self::itoa(h);
            let mut pal = s.clone();
            let mut rev_start = s.len() as i32 - 1;
            if n % 2 == 1 {
                rev_start -= 1;
            }
            let sb = s.as_bytes();
            let mut i = rev_start;
            while i >= 0 {
                pal.push(sb[i as usize] as char);
                i -= 1;
            }
            if Self::atoi_str(&pal) % k as i64 != 0 {
                continue;
            }
            let mut chars: Vec<u8> = pal.into_bytes();
            chars.sort_unstable();
            if seen.contains(&chars) {
                continue;
            }
            seen.insert(chars.clone());
            let mut cnt = [0i32; 10];
            for c in &chars {
                cnt[(c - b'0') as usize] += 1;
            }
            let mut total = fact[n as usize];
            for &c in &cnt {
                total /= fact[c as usize];
            }
            if cnt[0] > 0 {
                let mut bad = fact[n as usize - 1];
                cnt[0] -= 1;
                for &c in &cnt {
                    bad /= fact[c as usize];
                }
                cnt[0] += 1;
                total -= bad;
            }
            ans += total;
        }
        ans
    }
}
