// LeetCode 2180 - Count Integers With Even Digit Sum
// https://leetcode.com/problems/count-integers-with-even-digit-sum/

impl Solution {
    pub fn count_even(num: i32) -> i32 {
        let mut ans = 0;
        for x in 1..=num {
            let mut s = 0;
            let mut y = x;
            while y > 0 {
                s += y % 10;
                y /= 10;
            }
            if s % 2 == 0 {
                ans += 1;
            }
        }
        ans
    }
}
