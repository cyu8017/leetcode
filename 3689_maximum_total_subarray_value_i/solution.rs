// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

impl Solution {
    pub fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
        let mn = *nums.iter().min().unwrap();
        let mx = *nums.iter().max().unwrap();
        k as i64 * (mx - mn) as i64
    }
}
