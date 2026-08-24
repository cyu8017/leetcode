// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

impl Solution {
    pub fn maximums_spliced_array(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        fn kadane(a: &[i32], b: &[i32]) -> i32 {
            let mut best = 0;
            let mut cur = 0;
            let mut sum = 0;
            for i in 0..a.len() {
                sum += a[i];
                cur += b[i] - a[i];
                if cur < 0 {
                    cur = 0;
                }
                best = best.max(cur);
            }
            sum + best
        }
        kadane(&nums1, &nums2).max(kadane(&nums2, &nums1))
    }
}
