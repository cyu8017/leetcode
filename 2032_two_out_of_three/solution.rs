// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

use std::collections::HashSet;

impl Solution {
    pub fn two_out_of_three(nums1: Vec<i32>, nums2: Vec<i32>, nums3: Vec<i32>) -> Vec<i32> {
        let s0: HashSet<i32> = nums1.into_iter().collect();
        let s1: HashSet<i32> = nums2.into_iter().collect();
        let s2: HashSet<i32> = nums3.into_iter().collect();
        let mut ans = Vec::new();
        for v in 1..=100 {
            let c = s0.contains(&v) as i32 + s1.contains(&v) as i32 + s2.contains(&v) as i32;
            if c >= 2 {
                ans.push(v);
            }
        }
        ans
    }
}
