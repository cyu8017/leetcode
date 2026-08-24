// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

impl Solution {
    pub fn minimum_time(nums1: Vec<i32>, nums2: Vec<i32>, x: i32) -> i32 {
        let n = nums1.len();
        let mut arr: Vec<(i32, i32)> = (0..n).map(|i| (nums1[i], nums2[i])).collect();
        let sum1: i32 = nums1.iter().sum();
        let sum2: i32 = nums2.iter().sum();
        arr.sort_unstable_by_key(|a| a.1);
        let mut dp = vec![0i32; n + 1];
        for i in 0..n {
            for j in (1..=i + 1).rev() {
                dp[j] = dp[j].max(dp[j - 1] + arr[i].0 + j as i32 * arr[i].1);
            }
        }
        for t in 0..=n {
            if sum1 + sum2 * t as i32 - dp[t] <= x {
                return t as i32;
            }
        }
        -1
    }
}
