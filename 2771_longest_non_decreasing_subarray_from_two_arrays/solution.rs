// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

impl Solution {
    pub fn max_non_decreasing_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let mut dp1 = 1;
        let mut dp2 = 1;
        let mut ans = 1;
        for i in 1..n {
            let mut nd1 = 1;
            let mut nd2 = 1;
            if nums1[i] >= nums1[i - 1] {
                nd1 = nd1.max(dp1 + 1);
            }
            if nums1[i] >= nums2[i - 1] {
                nd1 = nd1.max(dp2 + 1);
            }
            if nums2[i] >= nums1[i - 1] {
                nd2 = nd2.max(dp1 + 1);
            }
            if nums2[i] >= nums2[i - 1] {
                nd2 = nd2.max(dp2 + 1);
            }
            dp1 = nd1;
            dp2 = nd2;
            ans = ans.max(dp1.max(dp2));
        }
        ans
    }
}
