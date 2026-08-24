// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

impl Solution {
    pub fn ways_to_split_array(nums: Vec<i32>) -> i32 {
        let total: i64 = nums.iter().map(|&v| v as i64).sum();
        let mut left = 0i64;
        let mut ans = 0;
        for i in 0..nums.len() - 1 {
            left += nums[i] as i64;
            if left >= total - left {
                ans += 1;
            }
        }
        ans
    }
}
