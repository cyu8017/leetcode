// LeetCode 0343 - Integer Break
// https://leetcode.com/problems/integer-break/

impl Solution {
    pub fn integer_break(n: i32) -> i32 {
        if n <= 3 {
            return n - 1;
        }

        let mut product = 1;
        let mut remaining = n;
        while remaining > 4 {
            product *= 3;
            remaining -= 3;
        }
        product * remaining
    }
}
