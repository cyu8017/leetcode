struct Solution;
// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

impl Solution {
    pub fn count_digit_occurrences(nums: Vec<i32>, digit: i32) -> i32 {
        let mut ans = 0;
        for mut x in nums {
            while x > 0 {
                if x % 10 == digit {
                    ans += 1;
                }
                x /= 10;
            }
        }
        ans
    }
}
