// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

use std::collections::HashMap;

impl Solution {
    pub fn num_triplets(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        fn count(a: &[i32], b: &[i32]) -> i32 {
            let mut squares = HashMap::new();
            for &x in a {
                *squares.entry(x as i64 * x as i64).or_insert(0) += 1;
            }
            let mut products = HashMap::new();
            for i in 0..b.len() {
                for j in i + 1..b.len() {
                    *products.entry(b[i] as i64 * b[j] as i64).or_insert(0) += 1;
                }
            }
            squares
                .iter()
                .map(|(value, &cnt)| cnt * products.get(value).copied().unwrap_or(0))
                .sum()
        }
        count(&nums1, &nums2) + count(&nums2, &nums1)
    }
}
