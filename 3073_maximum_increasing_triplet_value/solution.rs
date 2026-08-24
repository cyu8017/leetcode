// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

use std::collections::BTreeSet;

impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut right = vec![0; n];
        right[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            right[i] = nums[i].max(right[i + 1]);
        }
        let mut ts = BTreeSet::new();
        ts.insert(nums[0]);
        let mut ans = 0;
        for j in 1..n - 1 {
            if right[j + 1] > nums[j] {
                if let Some(&v) = ts.range(..nums[j]).next_back() {
                    ans = ans.max(v - nums[j] + right[j + 1]);
                }
            }
            ts.insert(nums[j]);
        }
        ans
    }
}
