struct Solution;

// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

impl Solution {
    pub fn closest_primes(left: i32, right: i32) -> Vec<i32> {
        let right = right as usize;
        let left = left as usize;
        let mut is_prime = vec![true; right + 1];
        if right >= 0 {
            is_prime[0] = false;
        }
        if right >= 1 {
            is_prime[1] = false;
        }
        let mut i = 2;
        while i * i <= right {
            if is_prime[i] {
                let mut j = i * i;
                while j <= right {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let primes: Vec<i32> = (left..=right)
            .filter(|&i| is_prime[i])
            .map(|i| i as i32)
            .collect();
        if primes.len() < 2 {
            return vec![-1, -1];
        }
        let mut best = vec![primes[0], primes[1]];
        let mut diff = primes[1] - primes[0];
        for i in 1..primes.len() - 1 {
            let d = primes[i + 1] - primes[i];
            if d < diff {
                diff = d;
                best = vec![primes[i], primes[i + 1]];
            }
        }
        best
    }
}

fn main() {}
