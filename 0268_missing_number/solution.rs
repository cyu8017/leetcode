// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let length = nums.len() as i32;
        let expected = length * (length + 1) / 2;
        let total: i32 = nums.iter().sum();
        expected - total
    }
}
