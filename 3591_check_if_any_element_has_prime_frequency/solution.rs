// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

use std::collections::HashMap;

impl Solution {
    fn is_prime(x: i32) -> bool {
        if x < 2 {
            return false;
        }
        let mut i = 2;
        while i * i <= x {
            if x % i == 0 {
                return false;
            }
            i += 1;
        }
        true
    }

    pub fn check_prime_frequency(nums: Vec<i32>) -> bool {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for x in nums {
            *cnt.entry(x).or_insert(0) += 1;
        }
        cnt.values().any(|&c| Self::is_prime(c))
    }
}
