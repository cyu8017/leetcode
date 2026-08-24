// LeetCode 2335 - Minimum Amount of Time to Fill Cups
// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

impl Solution {
    pub fn fill_cups(amount: Vec<i32>) -> i32 {
        let mut a = [amount[0], amount[1], amount[2]];
        a.sort_unstable();
        let (c, b, a) = (a[0], a[1], a[2]);
        if a >= b + c {
            a
        } else {
            (a + b + c + 1) / 2
        }
    }
}
