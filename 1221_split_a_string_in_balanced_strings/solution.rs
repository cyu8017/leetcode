// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        let mut balance = 0;
        let mut answer = 0;
        for ch in s.bytes() {
            if ch == b'L' {
                balance += 1;
            } else {
                balance -= 1;
            }
            if balance == 0 {
                answer += 1;
            }
        }
        answer
    }
}
