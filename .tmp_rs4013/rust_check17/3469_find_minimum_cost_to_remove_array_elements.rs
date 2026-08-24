struct Solution;
// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

use std::collections::HashMap;

impl Solution {
    fn max2(a: i32, b: i32) -> i32 {
        if a > b { a } else { b }
    }

    fn min3(a: i32, b: i32, c: i32) -> i32 {
        a.min(b).min(c)
    }

    fn dfs(i: usize, prev: i32, nums: &[i32], memo: &mut HashMap<(usize, i32), i32>) -> i32 {
        let n = nums.len();
        if i >= n {
            return if prev == -1 { 0 } else { nums[prev as usize] };
        }
        if let Some(&v) = memo.get(&(i, prev)) {
            return v;
        }
        let res = if prev == -1 {
            if i + 1 >= n {
                nums[i]
            } else if i + 2 >= n {
                Self::max2(nums[i], nums[i + 1])
            } else {
                let a = nums[i];
                let b = nums[i + 1];
                let c = nums[i + 2];
                Self::min3(
                    Self::max2(b, c) + Self::dfs(i + 3, i as i32, nums, memo),
                    Self::max2(a, c) + Self::dfs(i + 3, (i + 1) as i32, nums, memo),
                    Self::max2(a, b) + Self::dfs(i + 3, (i + 2) as i32, nums, memo),
                )
            }
        } else if i + 1 >= n {
            Self::max2(nums[prev as usize], nums[i])
        } else {
            let a = nums[prev as usize];
            let b = nums[i];
            let c = nums[i + 1];
            Self::min3(
                Self::max2(b, c) + Self::dfs(i + 2, prev, nums, memo),
                Self::max2(a, c) + Self::dfs(i + 2, i as i32, nums, memo),
                Self::max2(a, b) + Self::dfs(i + 2, (i + 1) as i32, nums, memo),
            )
        };
        memo.insert((i, prev), res);
        res
    }

    pub fn min_cost(nums: Vec<i32>) -> i32 {
        let mut memo = HashMap::new();
        Self::dfs(0, -1, &nums, &mut memo)
    }
}

fn main() {}
