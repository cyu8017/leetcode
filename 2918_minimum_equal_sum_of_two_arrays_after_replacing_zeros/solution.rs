// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let mut s1 = 0i64;
        let mut s2 = 0i64;
        let mut z1 = 0i32;
        let mut z2 = 0i32;
        for v in nums1 {
            if v == 0 {
                z1 += 1;
                s1 += 1;
            } else {
                s1 += v as i64;
            }
        }
        for v in nums2 {
            if v == 0 {
                z2 += 1;
                s2 += 1;
            } else {
                s2 += v as i64;
            }
        }
        if z1 == 0 && s1 < s2 {
            return -1;
        }
        if z2 == 0 && s2 < s1 {
            return -1;
        }
        s1.max(s2)
    }
}
