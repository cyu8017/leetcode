// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

impl Solution {
    pub fn prime_subarray(nums: Vec<i32>, k: i32) -> i32 {
        let mx = *nums.iter().max().unwrap_or(&0) as usize;
        let mut is_prime = vec![false; mx + 1];
        for i in 2..=mx {
            is_prime[i] = true;
        }
        let mut i = 2;
        while i * i <= mx {
            if is_prime[i] {
                let mut j = i * i;
                while j <= mx {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let n = nums.len();
        let mut ans = 0;
        for l in 0..n {
            let mut primes = Vec::new();
            for r in l..n {
                if is_prime[nums[r] as usize] {
                    primes.push(nums[r]);
                }
                if primes.len() >= 2 {
                    let mn = *primes.iter().min().unwrap();
                    let mxp = *primes.iter().max().unwrap();
                    if mxp - mn <= k {
                        ans += 1;
                    }
                }
            }
        }
        ans
    }
}
