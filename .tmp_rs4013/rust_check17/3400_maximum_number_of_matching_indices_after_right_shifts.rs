struct Solution;
// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

impl Solution {
    pub fn maximum_matching_indices(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let mut ans = 0;
        for shift in 0..n {
            let mut cnt = 0;
            for i in 0..n {
                if nums1[(i + n - shift) % n] == nums2[i] {
                    cnt += 1;
                }
            }
            if cnt > ans {
                ans = cnt;
            }
        }
        ans
    }
}

fn main() {}
