// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn count_nice_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut freq: HashMap<i32, i64> = HashMap::new();
        let mut ans = 0i64;

        for num in nums {
            let diff = num - Self::rev(num);
            ans = (ans + freq.get(&diff).copied().unwrap_or(0)) % MOD;
            *freq.entry(diff).or_insert(0) += 1;
        }

        ans as i32
    }

    fn rev(mut x: i32) -> i32 {
        let mut result = 0;
        while x > 0 {
            result = result * 10 + x % 10;
            x /= 10;
        }
        result
    }
}
