// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

use std::collections::HashSet;

impl Solution {
    pub fn split_array_same_average(mut nums: Vec<i32>) -> bool {
        let n = nums.len();
        let total: i32 = nums.iter().sum();
        nums.sort_unstable();
        let mut memo = HashSet::new();
        for size in 1..n {
            if total * size as i32 % n as i32 == 0
                && Self::find(&nums, total * size as i32 / n as i32, size as i32, 0, &mut memo)
            {
                return true;
            }
        }
        false
    }

    fn find(
        nums: &[i32],
        target: i32,
        count: i32,
        index: usize,
        memo: &mut HashSet<i64>,
    ) -> bool {
        if count == 0 {
            return target == 0;
        }
        let n = nums.len();
        if index == n || count as usize + index > n || target < 0 {
            return false;
        }
        let key = ((target as i64) << 20) | ((count as i64) << 10) | index as i64;
        if memo.contains(&key) {
            return false;
        }
        if Self::find(nums, target - nums[index], count - 1, index + 1, memo)
            || Self::find(nums, target, count, index + 1, memo)
        {
            return true;
        }
        memo.insert(key);
        false
    }
}
