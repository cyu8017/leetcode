// LeetCode 1413 - Minimum Value to Get Positive Step by Step Sum
// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

impl Solution {
    pub fn min_start_value(nums: Vec<i32>) -> i32 {
        let mut prefix = 0;
        let mut lowest = 0;
        for value in nums {
            prefix += value;
            lowest = lowest.min(prefix);
        }
        1 - lowest
    }
}
