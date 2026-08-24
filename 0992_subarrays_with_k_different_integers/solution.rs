// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

use std::collections::HashMap;

impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        fn at_most(nums: &[i32], m: i32) -> i32 {
            if m < 0 {
                return 0;
            }
            let mut count = HashMap::new();
            let mut left = 0;
            let mut ans = 0;
            for right in 0..nums.len() {
                *count.entry(nums[right]).or_insert(0) += 1;
                while count.len() as i32 > m {
                    let e = count.get_mut(&nums[left]).unwrap();
                    *e -= 1;
                    if *e == 0 {
                        count.remove(&nums[left]);
                    }
                    left += 1;
                }
                ans += (right - left + 1) as i32;
            }
            ans
        }
        at_most(&nums, k) - at_most(&nums, k - 1)
    }
}
