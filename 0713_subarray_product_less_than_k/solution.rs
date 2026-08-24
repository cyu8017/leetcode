// LeetCode 0713 - Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        if k <= 1 {
            return 0;
        }
        let mut product: i64 = 1;
        let mut left = 0;
        let mut ans = 0;
        for right in 0..nums.len() {
            product *= nums[right] as i64;
            while product >= k as i64 {
                product /= nums[left] as i64;
                left += 1;
            }
            ans += (right - left + 1) as i32;
        }
        ans
    }
}
