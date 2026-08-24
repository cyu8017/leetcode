// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

use std::collections::HashMap;

impl Solution {
    pub fn num_factored_binary_trees(mut arr: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        arr.sort_unstable();
        let mut dp = HashMap::new();
        for i in 0..arr.len() {
            let x = arr[i];
            let mut ways = 1i64;
            for j in 0..i {
                let left = arr[j];
                if x % left == 0 {
                    let right = x / left;
                    if let Some(&right_ways) = dp.get(&right) {
                        ways = (ways + dp[&left] * right_ways) % MOD;
                    }
                }
            }
            dp.insert(x, ways);
        }
        (dp.values().fold(0i64, |acc, &v| (acc + v) % MOD)) as i32
    }
}
