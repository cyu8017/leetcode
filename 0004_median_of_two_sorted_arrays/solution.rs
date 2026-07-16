// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

use std::cmp::{max, min};
use std::i32;

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let (nums1, nums2) = if nums1.len() > nums2.len() {
            (nums2, nums1)
        } else {
            (nums1, nums2)
        };

        let m = nums1.len();
        let n = nums2.len();
        let total_left = (m + n + 1) / 2;
        let mut lo = 0;
        let mut hi = m;

        while lo <= hi {
            let i = (lo + hi) / 2;
            let j = total_left - i;

            let nums1_left_max = if i == 0 { i32::MIN } else { nums1[i - 1] };
            let nums1_right_min = if i == m { i32::MAX } else { nums1[i] };
            let nums2_left_max = if j == 0 { i32::MIN } else { nums2[j - 1] };
            let nums2_right_min = if j == n { i32::MAX } else { nums2[j] };

            if nums1_left_max <= nums2_right_min && nums2_left_max <= nums1_right_min {
                if (m + n) % 2 == 1 {
                    return max(nums1_left_max, nums2_left_max) as f64;
                }
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) as f64
                    / 2.0;
            }

            if nums1_left_max > nums2_right_min {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }

        0.0
    }
}
