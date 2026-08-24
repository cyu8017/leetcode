// LeetCode 0660 - Remove 9
// https://leetcode.com/problems/remove-9/

impl Solution {
    pub fn new_integer(mut n: i32) -> i32 {
        let mut result = 0;
        let mut base = 1;
        while n > 0 {
            result += (n % 9) * base;
            n /= 9;
            base *= 10;
        }
        result
    }
}
