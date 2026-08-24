// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

impl Solution {
    pub fn abs_difference(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut ans = 0;
        let n = nums.len();
        for i in 0..k as usize {
            ans += nums[n - i - 1] - nums[i];
        }
        ans
    }
}
