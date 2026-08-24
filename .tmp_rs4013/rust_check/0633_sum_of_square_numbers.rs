struct Solution;
// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {
        let mut left: i64 = 0;
        let mut right = (c as f64).sqrt() as i64;
        while left <= right {
            let total = left * left + right * right;
            if total == c as i64 {
                return true;
            }
            if total < c as i64 {
                left += 1;
            } else {
                right -= 1;
            }
        }
        false
    }
}

fn main() {}
