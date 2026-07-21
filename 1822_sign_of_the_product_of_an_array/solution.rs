// LeetCode 1822 - Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/

impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut sign = 1;
        for num in nums {
            if num == 0 {
                return 0;
            }
            if num < 0 {
                sign = -sign;
            }
        }
        sign
    }
}
