// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

impl Solution {
    pub fn max_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut i = 0usize;
        let mut j = 0usize;
        let mut first = 0i64;
        let mut second = 0i64;
        while i < nums1.len() || j < nums2.len() {
            if j == nums2.len() || (i < nums1.len() && nums1[i] < nums2[j]) {
                first += nums1[i] as i64;
                i += 1;
            } else if i == nums1.len() || nums2[j] < nums1[i] {
                second += nums2[j] as i64;
                j += 1;
            } else {
                if first > second {
                    first += nums1[i] as i64;
                    second = first;
                } else {
                    second += nums1[i] as i64;
                    first = second;
                }
                i += 1;
                j += 1;
            }
        }
        (first.max(second) % 1_000_000_007) as i32
    }
}
