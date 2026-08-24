// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn max_frequency_score(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut a: i64, mut e: i64) -> i64 {
            let mut res = 1i64;
            a %= MOD;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                e >>= 1;
            }
            res
        }
        let k = k as usize;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut score = 0i64;
        let mut add = |freq: &mut HashMap<i32, i32>, score: &mut i64, x: i32| {
            let c = *freq.get(&x).unwrap_or(&0);
            if c > 0 {
                *score = (*score - mod_pow(x as i64, c as i64) + MOD) % MOD;
            }
            freq.insert(x, c + 1);
            *score = (*score + mod_pow(x as i64, (c + 1) as i64)) % MOD;
        };
        let mut remove = |freq: &mut HashMap<i32, i32>, score: &mut i64, x: i32| {
            let c = freq[&x];
            *score = (*score - mod_pow(x as i64, c as i64) + MOD) % MOD;
            if c == 1 {
                freq.remove(&x);
            } else {
                freq.insert(x, c - 1);
                *score = (*score + mod_pow(x as i64, (c - 1) as i64)) % MOD;
            }
        };
        let mut best = 0i64;
        for i in 0..nums.len() {
            add(&mut freq, &mut score, nums[i]);
            if i >= k {
                remove(&mut freq, &mut score, nums[i - k]);
            }
            if i + 1 >= k && score > best {
                best = score;
            }
        }
        best as i32
    }
}
