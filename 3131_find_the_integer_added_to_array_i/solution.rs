// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

impl Solution {
    pub fn added_integer(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        nums2.iter().copied().min().unwrap() - nums1.iter().copied().min().unwrap()
    }
}
