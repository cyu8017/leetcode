// LeetCode 1929 - Concatenation of Array
// https://leetcode.com/problems/concatenation-of-array/

impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = nums.clone();
        ans.extend_from_slice(&nums);
        ans
    }
}
