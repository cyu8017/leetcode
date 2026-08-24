// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

impl Solution {
    pub fn max_alternating_sum(mut nums: Vec<i32>) -> i64 {
        for x in nums.iter_mut() {
            *x *= *x;
        }
        nums.sort_unstable();
        let m = nums.len() / 2;
        let mut ans = 0i64;
        for i in 0..m {
            ans -= nums[i] as i64;
        }
        for i in m..nums.len() {
            ans += nums[i] as i64;
        }
        ans
    }
}
