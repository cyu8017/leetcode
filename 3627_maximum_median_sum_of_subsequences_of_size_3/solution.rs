// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

impl Solution {
    pub fn maximum_median_sum(mut nums: Vec<i32>) -> i64 {
        nums.sort_unstable();
        let n = nums.len();
        let mut ans = 0i64;
        let mut i = n / 3;
        while i < n {
            ans += nums[i] as i64;
            i += 2;
        }
        ans
    }
}
