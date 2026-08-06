// LeetCode 1458 - Max Dot Product of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

impl Solution {
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums2.len();
        let mut dp = vec![i32::MIN / 4; n + 1];
        for a in nums1 {
            let prev = dp.clone();
            for (j, &b) in nums2.iter().enumerate() {
                let j = j + 1;
                let product = a * b;
                dp[j] = dp[j - 1]
                    .max(prev[j])
                    .max(product)
                    .max(product + prev[j - 1].max(0));
            }
        }
        dp[n]
    }
}
