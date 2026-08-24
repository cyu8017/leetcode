struct Solution;
// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

use std::collections::HashMap;

impl Solution {
    pub fn min_length_after_removals(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut mx = 0i32;
        for v in nums {
            let e = freq.entry(v).or_insert(0);
            *e += 1;
            mx = mx.max(*e);
        }
        if mx <= n / 2 {
            return n % 2;
        }
        2 * mx - n
    }
}

fn main() {}
