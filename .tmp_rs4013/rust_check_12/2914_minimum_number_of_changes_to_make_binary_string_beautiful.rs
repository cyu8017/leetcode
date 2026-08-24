struct Solution;
// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

impl Solution {
    pub fn min_changes(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 0;
        let mut i = 0;
        while i < b.len() {
            if b[i] != b[i + 1] {
                ans += 1;
            }
            i += 2;
        }
        ans
    }
}

fn main() {}
