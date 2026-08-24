struct Solution;
// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

impl Solution {
    fn dfs(res: &mut [u8], i: usize, tight: bool, same_len: bool, num: &[u8], t: i64) -> bool {
        if i == res.len() {
            let mut prod = 1i64;
            for &c in res.iter() {
                prod *= (c - b'0') as i64;
                if prod == 0 {
                    break;
                }
            }
            return prod % t == 0 && prod > 0;
        }
        let mut start = if i == 0 { b'1' } else { b'0' };
        if tight && same_len && i < num.len() {
            start = num[i];
        }
        for c in start..=b'9' {
            res[i] = c;
            let nt = tight && same_len && i < num.len() && c == num[i];
            if Self::dfs(res, i + 1, nt, same_len, num, t) {
                return true;
            }
        }
        false
    }

    pub fn smallest_number(num: String, t: i64) -> String {
        let mut tt = t;
        for d in (2..=9).rev() {
            while tt % d == 0 {
                tt /= d;
            }
        }
        if tt > 1 {
            return "-1".to_string();
        }
        let nb = num.as_bytes();
        for extra in 0..=60 {
            let l = num.len() + extra;
            let mut res = vec![0u8; l];
            if Self::dfs(&mut res, 0, true, extra == 0, nb, t) {
                return String::from_utf8(res).unwrap();
            }
        }
        "-1".to_string()
    }
}

fn main() {}
