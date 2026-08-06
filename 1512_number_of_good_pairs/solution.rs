// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut freq = HashMap::new();
        let mut ans = 0;
        for x in nums {
            let c = freq.entry(x).or_insert(0);
            ans += *c;
            *c += 1;
        }
        ans
    }
}
