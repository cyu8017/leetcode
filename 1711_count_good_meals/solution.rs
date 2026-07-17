// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

use std::collections::HashMap;

impl Solution {
    pub fn count_pairs(deliciousness: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut seen: HashMap<i32, i64> = HashMap::new();
        let mut ans: i64 = 0;
        for &value in &deliciousness {
            for power in 0..22 {
                if let Some(&count) = seen.get(&((1 << power) - value)) {
                    ans += count;
                }
            }
            *seen.entry(value).or_insert(0) += 1;
        }
        (ans % MOD) as i32
    }
}
