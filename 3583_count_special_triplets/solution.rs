// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

use std::collections::HashMap;

impl Solution {
    pub fn special_triplets(nums: Vec<i32>) -> i32 {
        let mut left: HashMap<i32, i64> = HashMap::new();
        let mut right: HashMap<i32, i64> = HashMap::new();
        for &x in &nums {
            *right.entry(x).or_insert(0) += 1;
        }
        let mut ans = 0i64;
        const MOD: i64 = 1_000_000_007;
        for &x in &nums {
            *right.get_mut(&x).unwrap() -= 1;
            let l = *left.get(&(x * 2)).unwrap_or(&0);
            let r = *right.get(&(x * 2)).unwrap_or(&0);
            ans = (ans + l * r % MOD) % MOD;
            *left.entry(x).or_insert(0) += 1;
        }
        ans as i32
    }
}
