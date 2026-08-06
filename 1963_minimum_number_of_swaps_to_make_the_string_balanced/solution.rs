// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

impl Solution {
    pub fn min_swaps(s: String) -> i32 {
        let mut bal = 0;
        let mut mx = 0;
        for ch in s.chars() {
            if ch == '[' {
                bal += 1;
            } else {
                bal -= 1;
            }
            mx = mx.min(bal);
        }
        (-mx + 1) / 2
    }
}
