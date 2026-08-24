// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

use std::collections::HashMap;

impl Solution {
    pub fn sum_divisible_by_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut cnt = HashMap::new();
        for x in nums {
            *cnt.entry(x).or_insert(0) += 1;
        }
        let mut ans = 0;
        for (x, v) in cnt {
            if v % k == 0 {
                ans += x * v;
            }
        }
        ans
    }
}
