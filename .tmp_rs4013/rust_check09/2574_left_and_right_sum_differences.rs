struct Solution;

// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

impl Solution {
    pub fn left_right_difference(nums: Vec<i32>) -> Vec<i32> {
        let total: i32 = nums.iter().sum();
        let mut ans = vec![0; nums.len()];
        let mut left = 0;
        for i in 0..nums.len() {
            let right = total - left - nums[i];
            ans[i] = (left - right).abs();
            left += nums[i];
        }
        ans
    }
}

fn main() {}
