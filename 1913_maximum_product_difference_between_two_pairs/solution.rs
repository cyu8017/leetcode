// LeetCode 1913 - Maximum Product Difference Between Two Pairs
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        let mut a = 0;
        let mut b = 0;
        let mut c = 100_000;
        let mut d = 100_000;
        for x in nums {
            if x > a {
                b = a;
                a = x;
            } else if x > b {
                b = x;
            }
            if x < c {
                d = c;
                c = x;
            } else if x < d {
                d = x;
            }
        }
        a * b - c * d
    }
}
