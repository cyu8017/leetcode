// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

impl Solution {
    pub fn minimum_moves(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut ans = 0;
        let mut i = 0;
        while i < bytes.len() {
            if bytes[i] == b'X' {
                ans += 1;
                i += 3;
            } else {
                i += 1;
            }
        }
        ans
    }
}
