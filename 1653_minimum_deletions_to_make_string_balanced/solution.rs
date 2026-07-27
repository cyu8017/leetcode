// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {
        let mut b = 0;
        let mut ans = 0;
        for c in s.bytes() {
            if c == b'b' {
                b += 1;
            } else {
                ans = (ans + 1).min(b);
            }
        }
        ans
    }
}
