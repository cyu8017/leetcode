// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

use std::collections::HashSet;

impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {
        let primes: HashSet<u32> = [2, 3, 5, 7, 11, 13, 17, 19].into_iter().collect();
        (left..=right)
            .filter(|&num| primes.contains(&(num as u32).count_ones()))
            .count() as i32
    }
}
