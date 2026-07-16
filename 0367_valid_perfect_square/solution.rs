// LeetCode 0367 - Valid Perfect Square
// https://leetcode.com/problems/valid-perfect-square/

impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        let mut left = 1i64;
        let mut right = num as i64;

        while left <= right {
            let mid = left + (right - left) / 2;
            let square = mid * mid;
            if square == num as i64 {
                return true;
            }
            if square < num as i64 {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        false
    }
}
