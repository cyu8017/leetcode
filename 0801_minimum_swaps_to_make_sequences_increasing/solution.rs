// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

impl Solution {
    pub fn min_swap(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let mut swap = vec![n as i32; n];
        let mut keep = vec![n as i32; n];
        swap[0] = 1;
        keep[0] = 0;
        for i in 1..n {
            if nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1] {
                keep[i] = keep[i - 1];
                swap[i] = swap[i - 1] + 1;
            }
            if nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1] {
                keep[i] = keep[i].min(swap[i - 1]);
                swap[i] = swap[i].min(keep[i - 1] + 1);
            }
        }
        swap[n - 1].min(keep[n - 1])
    }
}
