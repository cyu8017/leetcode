// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

impl Solution {
    pub fn sum_indices_with_k_set_bits(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        for (i, &v) in nums.iter().enumerate() {
            let mut bits = 0;
            let mut x = i;
            while x > 0 {
                bits += (x & 1) as i32;
                x >>= 1;
            }
            if bits == k {
                ans += v;
            }
        }
        ans
    }
}
