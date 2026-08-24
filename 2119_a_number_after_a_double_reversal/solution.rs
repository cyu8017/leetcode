// LeetCode 2119 - A Number After a Double Reversal
// https://leetcode.com/problems/a-number-after-a-double-reversal/

impl Solution {
    pub fn is_same_after_reversals(num: i32) -> bool {
        num == 0 || num % 10 != 0
    }
}
