// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn ways_to_partition(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut pref = vec![0i64; n];
        pref[0] = nums[0] as i64;
        for i in 1..n {
            pref[i] = pref[i - 1] + nums[i] as i64;
        }
        let total = pref[n - 1];
        let mut right = HashMap::new();
        let mut left = HashMap::new();
        for i in 0..n - 1 {
            *right.entry(pref[i]).or_insert(0) += 1;
        }
        let mut ans = 0;
        if total % 2 == 0 {
            ans = *right.get(&(total / 2)).unwrap_or(&0);
        }
        for i in 0..n {
            let diff = k as i64 - nums[i] as i64;
            let new_total = total + diff;
            let mut cur = 0;
            if new_total % 2 == 0 {
                let half = new_total / 2;
                cur = left.get(&half).unwrap_or(&0) + right.get(&(half - diff)).unwrap_or(&0);
            }
            ans = ans.max(cur);
            if i < n - 1 {
                *left.entry(pref[i]).or_insert(0) += 1;
                *right.entry(pref[i]).or_insert(0) -= 1;
            }
        }
        ans
    }
}
