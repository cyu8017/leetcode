// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

impl Solution {
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut streak = 0i64;
        for x in nums {
            if x == 0 {
                streak += 1;
                ans += streak;
            } else {
                streak = 0;
            }
        }
        ans
    }
}
