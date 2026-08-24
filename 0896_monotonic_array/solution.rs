// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

impl Solution {
    pub fn is_monotonic(nums: Vec<i32>) -> bool {
        let mut inc = true;
        let mut dec = true;
        for i in 1..nums.len() {
            if nums[i] < nums[i - 1] {
                inc = false;
            }
            if nums[i] > nums[i - 1] {
                dec = false;
            }
        }
        inc || dec
    }
}
