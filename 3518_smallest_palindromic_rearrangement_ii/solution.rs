// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

impl Solution {
    const MAX: i32 = 1_000_001;

    fn n_ck(n: i32, mut kk: i32) -> i32 {
        if kk < 0 || kk > n {
            return 0;
        }
        let mut res: i64 = 1;
        if kk > n - kk {
            kk = n - kk;
        }
        for i in 1..=kk {
            res = res * (n - i + 1) as i64 / i as i64;
            if res >= Self::MAX as i64 {
                return Self::MAX;
            }
        }
        res as i32
    }

    fn count_arr(h: &[i32]) -> i32 {
        let mut total: i32 = h.iter().sum();
        let mut res: i64 = 1;
        for &f in h {
            res *= Self::n_ck(total, f) as i64;
            if res >= Self::MAX as i64 {
                return Self::MAX;
            }
            total -= f;
        }
        res as i32
    }

    pub fn smallest_palindrome(s: String, mut k: i32) -> String {
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let odd = cnt.iter().filter(|&&c| c % 2 == 1).count();
        if odd > 1 {
            return String::new();
        }
        let mut half = [0i32; 26];
        let mut mid = 0u8;
        for i in 0..26 {
            half[i] = cnt[i] / 2;
            if cnt[i] % 2 == 1 {
                mid = b'a' + i as u8;
            }
        }
        if Self::count_arr(&half) < k {
            return String::new();
        }
        let half_len: i32 = half.iter().sum();
        let mut left = String::new();
        for _ in 0..half_len {
            for i in 0..26 {
                if half[i] == 0 {
                    continue;
                }
                half[i] -= 1;
                let arr = Self::count_arr(&half);
                if arr >= k {
                    left.push((b'a' + i as u8) as char);
                    break;
                }
                k -= arr;
                half[i] += 1;
            }
        }
        let mut res = left.clone();
        if mid != 0 {
            res.push(mid as char);
        }
        for c in left.chars().rev() {
            res.push(c);
        }
        res
    }
}
