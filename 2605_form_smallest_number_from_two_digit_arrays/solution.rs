// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

use std::collections::HashSet;

impl Solution {
    pub fn min_number(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let s1: HashSet<i32> = nums1.iter().copied().collect();
        let s2: HashSet<i32> = nums2.iter().copied().collect();
        let mut best_shared = 10;
        for d in 1..=9 {
            if s1.contains(&d) && s2.contains(&d) && d < best_shared {
                best_shared = d;
            }
        }
        if best_shared < 10 {
            return best_shared;
        }
        let m1 = *nums1.iter().min().unwrap();
        let m2 = *nums2.iter().min().unwrap();
        if m1 < m2 {
            m1 * 10 + m2
        } else {
            m2 * 10 + m1
        }
    }
}
