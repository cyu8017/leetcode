// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        let mut bits = 0;
        for &num in &nums {
            bits |= num;
        }
        let mut total = 0;
        let mut bit = 1;
        while bit <= bits {
            if bits & bit != 0 {
                total += bit;
            }
            bit <<= 1;
        }
        total << (nums.len() - 1)
    }
}
