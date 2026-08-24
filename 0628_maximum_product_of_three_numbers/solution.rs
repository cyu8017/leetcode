// LeetCode 0628 - Maximum Product of Three Numbers
// https://leetcode.com/problems/maximum-product-of-three-numbers/

impl Solution {
    pub fn maximum_product(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let a = nums[n - 1] as i64 * nums[n - 2] as i64 * nums[n - 3] as i64;
        let b = nums[0] as i64 * nums[1] as i64 * nums[n - 1] as i64;
        a.max(b) as i32
    }
}
