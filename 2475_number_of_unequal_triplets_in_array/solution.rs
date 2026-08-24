// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

use std::collections::HashMap;

impl Solution {
    pub fn unequal_triplets(nums: Vec<i32>) -> i32 {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for x in &nums {
            *cnt.entry(*x).or_insert(0) += 1;
        }
        let mut ans = 0;
        let n = nums.len() as i32;
        let mut left = 0;
        for &c in cnt.values() {
            let right = n - left - c;
            ans += left * c * right;
            left += c;
        }
        ans
    }
}
