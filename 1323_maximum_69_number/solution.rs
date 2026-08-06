// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

impl Solution {
    pub fn maximum69_number(num: i32) -> i32 {
        num.to_string().replacen('6', "9", 1).parse().unwrap()
    }
}
