// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

impl Solution {
    pub fn min_product_sum(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> i32 {
        nums1.sort_unstable();
        nums2.sort_unstable_by(|a, b| b.cmp(a));
        nums1.iter().zip(nums2.iter()).map(|(a, b)| a * b).sum()
    }
}
