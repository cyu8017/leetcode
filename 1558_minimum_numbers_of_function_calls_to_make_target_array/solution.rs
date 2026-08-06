// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let adds: i32 = nums.iter().map(|x| x.count_ones() as i32).sum();
        let shifts = nums
            .iter()
            .map(|x| if *x == 0 { 0 } else { 31 - x.leading_zeros() as i32 })
            .max()
            .unwrap_or(0);
        adds + shifts
    }
}
