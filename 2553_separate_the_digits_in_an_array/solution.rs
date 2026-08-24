// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

impl Solution {
    pub fn separate_digits(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();
        for mut x in nums {
            let mut digits = Vec::new();
            while x > 0 {
                digits.push(x % 10);
                x /= 10;
            }
            for d in digits.into_iter().rev() {
                ans.push(d);
            }
        }
        ans
    }
}
