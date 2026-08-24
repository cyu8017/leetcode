// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

use std::collections::HashSet;

impl Solution {
    pub fn maximum_set_size(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let s1: HashSet<i32> = nums1.iter().copied().collect();
        let s2: HashSet<i32> = nums2.iter().copied().collect();
        let mut a = 0;
        let mut b = 0;
        let mut c = 0;
        for &x in &s1 {
            if !s2.contains(&x) {
                a += 1;
            }
        }
        for &x in &s2 {
            if !s1.contains(&x) {
                b += 1;
            } else {
                c += 1;
            }
        }
        let n = nums1.len() as i32;
        a = a.min(n / 2);
        b = b.min(n / 2);
        (a + b + c).min(n)
    }
}
