// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for mut value in nums {
            let mut digits = 0;
            while value > 0 {
                value /= 10;
                digits += 1;
            }
            if digits % 2 == 0 {
                ans += 1;
            }
        }
        ans
    }
}
