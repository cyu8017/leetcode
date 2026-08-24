// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

impl Solution {
    pub fn find_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let m = nums1.len();
        let n = nums2.len();
        let mut dp = vec![0; n + 1];
        let mut best = 0;
        for i in 1..=m {
            let mut next = vec![0; n + 1];
            for j in 1..=n {
                if nums1[i - 1] == nums2[j - 1] {
                    next[j] = dp[j - 1] + 1;
                    best = best.max(next[j]);
                }
            }
            dp = next;
        }
        best
    }
}
