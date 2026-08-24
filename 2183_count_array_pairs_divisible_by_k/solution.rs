// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

use std::collections::HashMap;

impl Solution {
    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }

    pub fn count_pairs(nums: Vec<i32>, k: i32) -> i64 {
        let mut freq = HashMap::new();
        let mut ans = 0i64;
        for x in nums {
            let g1 = Self::gcd(x, k);
            for (&g2, &c) in &freq {
                if (g1 as i64 * g2 as i64) % k as i64 == 0 {
                    ans += c as i64;
                }
            }
            *freq.entry(g1).or_insert(0) += 1;
        }
        ans
    }
}
