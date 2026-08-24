struct Solution;
// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len().saturating_sub(2) {
            if nums[i] * 2 + nums[i + 2] * 2 == nums[i + 1] {
                ans += 1;
            }
        }
        ans
    }
}

fn main() {}
