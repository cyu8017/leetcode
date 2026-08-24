// LeetCode 2310 - Sum of Numbers With Units Digit K
// https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

impl Solution {
    pub fn minimum_numbers(num: i32, k: i32) -> i32 {
        if num == 0 {
            return 0;
        }
        for count in 1..=10 {
            if count * k % 10 == num % 10 && count * k <= num {
                return count;
            }
        }
        -1
    }
}
