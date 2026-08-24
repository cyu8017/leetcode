// LeetCode 0976 - Largest Perimeter Triangle
// https://leetcode.com/problems/largest-perimeter-triangle/

impl Solution {
    pub fn largest_perimeter(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable_by(|a, b| b.cmp(a));
        for i in 0..nums.len().saturating_sub(2) {
            if nums[i] < nums[i + 1] + nums[i + 2] {
                return nums[i] + nums[i + 1] + nums[i + 2];
            }
        }
        0
    }
}
