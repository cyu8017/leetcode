// LeetCode 0088 - Merge Sorted Array
// https://leetcode.com/problems/merge-sorted-array/

impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut i = m - 1;
        let mut j = n - 1;
        let mut write = m + n - 1;

        while j >= 0 {
            if i >= 0 && nums1[i as usize] > nums2[j as usize] {
                nums1[write as usize] = nums1[i as usize];
                i -= 1;
            } else {
                nums1[write as usize] = nums2[j as usize];
                j -= 1;
            }
            write -= 1;
        }
    }
}
