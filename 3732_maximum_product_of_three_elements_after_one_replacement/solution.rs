// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

impl Solution {
    pub fn max_product(mut nums: Vec<i32>) -> i64 {
        nums.sort_unstable();
        let n = nums.len();
        let a = nums[0] as i64;
        let b = nums[1] as i64;
        let c = nums[n - 2] as i64;
        let d = nums[n - 1] as i64;
        const X: i64 = 100000;
        (a * b * X).max(c * d * X).max(-a * d * X)
    }
}
