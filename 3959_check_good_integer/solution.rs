// LeetCode 3959 - Check Good Integer
// https://leetcode.com/problems/check-good-integer/

impl Solution {
    pub fn check_good_integer(mut n: i32) -> bool {
        let mut s = 0;
        while n > 0 {
            let x = n % 10;
            s += x * (x - 1);
            n /= 10;
        }
        s >= 50
    }
}
