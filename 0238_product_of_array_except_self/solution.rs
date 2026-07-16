// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let length = nums.len();
        let mut result = vec![1; length];
        let mut prefix = 1;
        for index in 0..length {
            result[index] = prefix;
            prefix *= nums[index];
        }
        let mut suffix = 1;
        for index in (0..length).rev() {
            result[index] *= suffix;
            suffix *= nums[index];
        }
        result
    }
}
