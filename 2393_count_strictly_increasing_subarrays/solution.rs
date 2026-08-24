// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut len = 0i64;
        for i in 0..nums.len() {
            if i > 0 && nums[i] > nums[i - 1] {
                len += 1;
            } else {
                len = 1;
            }
            ans += len;
        }
        ans
    }
}
