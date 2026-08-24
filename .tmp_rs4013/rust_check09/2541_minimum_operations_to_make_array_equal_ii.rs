struct Solution;

// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

impl Solution {
    pub fn min_operations(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        if k == 0 {
            for i in 0..nums1.len() {
                if nums1[i] != nums2[i] {
                    return -1;
                }
            }
            return 0;
        }
        let mut pos = 0i64;
        let mut neg = 0i64;
        for i in 0..nums1.len() {
            let d = nums1[i] - nums2[i];
            if d % k != 0 {
                return -1;
            }
            if d > 0 {
                pos += (d / k) as i64;
            } else {
                neg += ((-d) / k) as i64;
            }
        }
        if pos != neg {
            -1
        } else {
            pos
        }
    }
}

fn main() {}
