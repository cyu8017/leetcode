struct Solution;
// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

impl Solution {
    pub fn minimum_average(mut nums: Vec<i32>) -> f64 {
        nums.sort_unstable();
        let n = nums.len();
        let mut ans = 1 << 30;
        for i in 0..n / 2 {
            ans = ans.min(nums[i] + nums[n - i - 1]);
        }
        ans as f64 / 2.0
    }
}

fn main() {}
