// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

use std::collections::HashSet;

impl Solution {
    pub fn distinct_prime_factors(nums: Vec<i32>) -> i32 {
        let mut set = HashSet::new();
        for mut x in nums {
            let mut p = 2;
            while p * p <= x {
                if x % p == 0 {
                    set.insert(p);
                    while x % p == 0 {
                        x /= p;
                    }
                }
                p += 1;
            }
            if x > 1 {
                set.insert(x);
            }
        }
        set.len() as i32
    }
}
