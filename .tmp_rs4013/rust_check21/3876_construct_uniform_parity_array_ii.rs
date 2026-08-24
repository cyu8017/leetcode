struct Solution;
// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

impl Solution {
    pub fn uniform_array(nums1: Vec<i32>) -> bool {
        let mut mn = i32::MAX;
        for &x in &nums1 {
            if x % 2 == 1 && x < mn {
                mn = x;
            }
        }
        for &x in &nums1 {
            if x % 2 == 0 && mn != i32::MAX && x < mn {
                return false;
            }
        }
        true
    }
}
