// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

impl Solution {
    pub fn self_dividing_numbers(left: i32, right: i32) -> Vec<i32> {
        (left..=right).filter(|&num| Self::is_self_dividing(num)).collect()
    }

    fn is_self_dividing(num: i32) -> bool {
        let mut x = num;
        while x != 0 {
            let digit = x % 10;
            if digit == 0 || num % digit != 0 {
                return false;
            }
            x /= 10;
        }
        true
    }
}
