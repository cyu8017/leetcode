// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

impl Solution {
    pub fn subtract_product_and_sum(mut n: i32) -> i32 {
        let mut product = 1;
        let mut total = 0;
        while n > 0 {
            let digit = n % 10;
            n /= 10;
            product *= digit;
            total += digit;
        }
        product - total
    }
}
