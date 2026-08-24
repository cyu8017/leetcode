// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

impl Solution {
    pub fn last_remaining(mut n: i64) -> i64 {
        let mut first = 1i64;
        let mut step = 2i64;
        let mut left = true;
        while n > 1 {
            if !left && n % 2 == 0 {
                first += step;
            }
            n = (n + 1) / 2;
            step *= 2;
            left = !left;
        }
        first
    }
}
