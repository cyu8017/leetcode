// LeetCode 1920 - Build Array from Permutation
// https://leetcode.com/problems/build-array-from-permutation/

impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        nums.iter().map(|&x| nums[x as usize]).collect()
    }
}
