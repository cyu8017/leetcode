// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i64) -> i64 {
        let mut ans = 0i64;
        let mut sum = 0i64;
        let mut left = 0usize;
        for right in 0..nums.len() {
            sum += nums[right] as i64;
            while sum * (right as i64 - left as i64 + 1) >= k {
                sum -= nums[left] as i64;
                left += 1;
            }
            ans += right as i64 - left as i64 + 1;
        }
        ans
    }
}
