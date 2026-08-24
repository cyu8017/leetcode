// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

use std::collections::BTreeMap;

impl Solution {
    pub fn max_sum(nums: Vec<i32>, threshold: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| threshold[i]);
        let mut tree: BTreeMap<i32, i32> = BTreeMap::new();
        let mut ans = 0i64;
        let mut i = 0usize;
        let mut step = 1i32;
        loop {
            while i < n && threshold[idx[i]] <= step {
                *tree.entry(nums[idx[i]]).or_insert(0) += 1;
                i += 1;
            }
            if tree.is_empty() {
                break;
            }
            let mx = *tree.keys().next_back().unwrap();
            ans += mx as i64;
            if let Some(c) = tree.get_mut(&mx) {
                *c -= 1;
                if *c == 0 {
                    tree.remove(&mx);
                }
            }
            step += 1;
        }
        ans
    }
}
