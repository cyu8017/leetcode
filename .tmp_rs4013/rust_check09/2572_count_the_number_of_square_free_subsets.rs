struct Solution;

// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

use std::collections::HashMap;

impl Solution {
    pub fn square_free_subsets(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        let mask_of = |mut x: i32| -> i32 {
            let mut mask = 0;
            for (i, &p) in primes.iter().enumerate() {
                let mut cnt = 0;
                while x % p == 0 {
                    x /= p;
                    cnt += 1;
                    if cnt > 1 {
                        return -1;
                    }
                }
                if cnt == 1 {
                    mask |= 1 << i;
                }
            }
            mask
        };
        let mut freq = HashMap::new();
        for x in nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut dp = vec![0i64; 1 << 10];
        dp[0] = 1;
        for (&x, &c) in &freq {
            if x == 1 {
                continue;
            }
            let m = mask_of(x);
            if m < 0 {
                continue;
            }
            let m = m as usize;
            for state in (0..(1 << 10)).rev() {
                if state & m == 0 {
                    dp[state | m] = (dp[state | m] + dp[state] * c as i64) % MOD;
                }
            }
        }
        let mut ans = 0i64;
        for v in dp {
            ans = (ans + v) % MOD;
        }
        let ones = *freq.get(&1).unwrap_or(&0);
        let mut mul = 1i64;
        for _ in 0..ones {
            mul = mul * 2 % MOD;
        }
        ans = ans * mul % MOD;
        ans = (ans - 1 + MOD) % MOD;
        ans as i32
    }
}

fn main() {}
