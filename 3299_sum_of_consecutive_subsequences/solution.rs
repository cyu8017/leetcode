// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

use std::collections::HashMap;

impl Solution {
    pub fn range_sum(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut sum: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0i32;
        for x in nums {
            let cl = *cnt.get(&(x - 1)).unwrap_or(&0);
            let sl = *sum.get(&(x - 1)).unwrap_or(&0);
            let cr = *cnt.get(&(x + 1)).unwrap_or(&0);
            let sr = *sum.get(&(x + 1)).unwrap_or(&0);
            let mut c = ((1 + cl as i64 + cr as i64) % MOD) as i32;
            let mut s = ((x as i64 + sl as i64 + cl as i64 * x as i64 % MOD + sr as i64 + cr as i64 * x as i64 % MOD) % MOD) as i32;
            if cl > 0 && cr > 0 {
                c = ((c as i64 + cl as i64 * cr as i64 % MOD) % MOD) as i32;
                s = ((s as i64 + sl as i64 * cr as i64 % MOD + sr as i64 * cl as i64 % MOD + cl as i64 * cr as i64 % MOD * x as i64 % MOD) % MOD) as i32;
            }
            *cnt.entry(x).or_insert(0) = ((*cnt.get(&x).unwrap_or(&0) as i64 + c as i64) % MOD) as i32;
            *sum.entry(x).or_insert(0) = ((*sum.get(&x).unwrap_or(&0) as i64 + s as i64) % MOD) as i32;
            ans = ((ans as i64 + s as i64) % MOD) as i32;
        }
        ans
    }
}
