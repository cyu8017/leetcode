// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut ops = 0;
        let mut prev = nums[0];
        for &value in &nums[1..] {
            if value <= prev {
                let needed = prev + 1;
                ops += needed - value;
                prev = needed;
            } else {
                prev = value;
            }
        }
        ops
    }
}
