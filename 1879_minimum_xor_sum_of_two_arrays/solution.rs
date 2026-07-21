// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

impl Solution {
    pub fn minimum_xor_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let mut dp = vec![i32::MAX; 1 << n];
        dp[0] = 0;
        for mask in 0usize..(1 << n) {
            let i = mask.count_ones() as usize;
            if i >= n {
                continue;
            }
            for j in 0..n {
                if mask & (1 << j) != 0 {
                    continue;
                }
                let next_mask = mask | (1 << j);
                let cost = dp[mask].saturating_add(nums1[i] ^ nums2[j]);
                if cost < dp[next_mask] {
                    dp[next_mask] = cost;
                }
            }
        }
        dp[(1 << n) - 1]
    }
}
