struct Solution;
// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

use std::collections::HashMap;

impl Solution {
    pub fn sum_of_good_subsequences(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut sum: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0i32;
        for x in nums {
            let mut c = 1i32;
            let mut s = x;
            if *cnt.get(&(x - 1)).unwrap_or(&0) > 0 {
                c = ((c as i64 + *cnt.get(&(x - 1)).unwrap() as i64) % MOD) as i32;
                s = ((s as i64 + *sum.get(&(x - 1)).unwrap() as i64 + *cnt.get(&(x - 1)).unwrap() as i64 * x as i64 % MOD) % MOD) as i32;
            }
            if *cnt.get(&(x + 1)).unwrap_or(&0) > 0 {
                c = ((c as i64 + *cnt.get(&(x + 1)).unwrap() as i64) % MOD) as i32;
                s = ((s as i64 + *sum.get(&(x + 1)).unwrap() as i64 + *cnt.get(&(x + 1)).unwrap() as i64 * x as i64 % MOD) % MOD) as i32;
            }
            *cnt.entry(x).or_insert(0) = ((*cnt.get(&x).unwrap_or(&0) as i64 + c as i64) % MOD) as i32;
            *sum.entry(x).or_insert(0) = ((*sum.get(&x).unwrap_or(&0) as i64 + s as i64) % MOD) as i32;
            ans = ((ans as i64 + s as i64) % MOD) as i32;
        }
        ans
    }
}

fn main() {}
