// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

impl Solution {
    pub fn non_special_count(l: i32, r: i32) -> i32 {
        const M: usize = 31623;
        let mut primes = vec![true; M + 1];
        primes[0] = false;
        primes[1] = false;
        for i in 2..=M {
            if primes[i] {
                let mut j = i * 2;
                while j <= M {
                    primes[j] = false;
                    j += i;
                }
            }
        }
        let lo = (l as f64).sqrt().ceil() as i32;
        let hi = (r as f64).sqrt().floor() as i32;
        let mut cnt = 0;
        for i in lo..=hi {
            if primes[i as usize] {
                cnt += 1;
            }
        }
        r - l + 1 - cnt
    }
}
