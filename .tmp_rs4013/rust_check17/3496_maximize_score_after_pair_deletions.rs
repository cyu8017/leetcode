struct Solution;
// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

impl Solution {
    pub fn maximize_score(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let total: i32 = nums.iter().sum();
        if n % 2 == 1 {
            let mn = *nums.iter().min().unwrap();
            return total - mn;
        }
        let mut mn = nums[0] + nums[1];
        for i in 0..n - 1 {
            mn = mn.min(nums[i] + nums[i + 1]);
        }
        total - mn
    }
}

fn main() {}
