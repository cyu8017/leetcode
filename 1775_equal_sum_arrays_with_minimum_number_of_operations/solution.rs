// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

impl Solution {
    pub fn min_operations(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        if nums1.len() * 6 < nums2.len() || nums2.len() * 6 < nums1.len() {
            return -1;
        }
        let mut s1: i32 = nums1.iter().sum();
        let mut s2: i32 = nums2.iter().sum();
        if s1 == s2 {
            return 0;
        }
        let (mut big, mut small) = (nums1, nums2);
        if s1 < s2 {
            std::mem::swap(&mut big, &mut small);
            std::mem::swap(&mut s1, &mut s2);
        }
        let mut diff = s1 - s2;
        let mut gains: Vec<i32> = big
            .iter()
            .map(|&x| x - 1)
            .chain(small.iter().map(|&x| 6 - x))
            .collect();
        gains.sort_unstable_by(|a, b| b.cmp(a));
        let mut ops = 0;
        for gain in gains {
            if diff <= 0 {
                break;
            }
            diff -= gain;
            ops += 1;
        }
        if diff <= 0 {
            ops
        } else {
            -1
        }
    }
}
