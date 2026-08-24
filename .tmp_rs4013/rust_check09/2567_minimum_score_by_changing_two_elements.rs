struct Solution;

// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

impl Solution {
    pub fn minimize_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let a = nums[n - 1] - nums[2];
        let b = nums[n - 3] - nums[0];
        let c = nums[n - 2] - nums[1];
        a.min(b).min(c)
    }
}

fn main() {}
