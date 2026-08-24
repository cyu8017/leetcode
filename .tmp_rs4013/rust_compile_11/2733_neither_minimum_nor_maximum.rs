struct Solution;
fn main() {}

// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

impl Solution {
    pub fn find_non_min_or_max(nums: Vec<i32>) -> i32 {
        if nums.len() < 3 {
            return -1;
        }
        let (a, b, c) = (nums[0], nums[1], nums[2]);
        a + b + c - a.max(b).max(c) - a.min(b).min(c)
    }
}
