// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

impl Solution {
    pub fn even_product(nums: Vec<i32>) -> i64 {
        let n = nums.len() as i64;
        let total = n * (n + 1) / 2;
        let mut odd_len = 0i64;
        let mut odd = 0i64;
        for x in nums {
            if x % 2 == 1 {
                odd += 1;
                odd_len += odd;
            } else {
                odd = 0;
            }
        }
        total - odd_len
    }
}
