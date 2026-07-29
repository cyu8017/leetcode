// LeetCode 1085 - Sum of Digits in the Minimum Number
// https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

impl Solution {
    pub fn sum_of_digits(nums: Vec<i32>) -> i32 {
        let mut n = *nums.iter().min().unwrap();
        let mut digit_sum = 0;
        while n > 0 {
            digit_sum += n % 10;
            n /= 10;
        }
        if digit_sum % 2 == 0 {
            1
        } else {
            0
        }
    }
}
