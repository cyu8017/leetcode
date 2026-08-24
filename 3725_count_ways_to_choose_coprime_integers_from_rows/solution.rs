// LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

use std::collections::HashMap;

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

impl Solution {
    pub fn count_coprime(mat: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = mat.len();
        let mut dp: HashMap<i32, i32> = HashMap::new();
        for &v in &mat[0] {
            *dp.entry(v).or_insert(0) += 1;
        }
        for i in 1..m {
            let mut ndp: HashMap<i32, i32> = HashMap::new();
            for &v in &mat[i] {
                for (&g, &cnt) in &dp {
                    let ng = gcd(g, v);
                    *ndp.entry(ng).or_insert(0) = (ndp.get(&ng).copied().unwrap_or(0) + cnt) % MOD;
                }
            }
            dp = ndp;
        }
        dp.get(&1).copied().unwrap_or(0)
    }
}
