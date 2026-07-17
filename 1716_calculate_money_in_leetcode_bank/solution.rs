// LeetCode 1716 - Calculate Money in Leetcode Bank
// https://leetcode.com/problems/calculate-money-in-leetcode-bank/

impl Solution {
    pub fn total_money(n: i32) -> i32 {
        let weeks = n / 7;
        let days = n % 7;
        weeks * 28 + 7 * weeks * (weeks - 1) / 2 + days * (weeks + 1) + days * (days - 1) / 2
    }
}
