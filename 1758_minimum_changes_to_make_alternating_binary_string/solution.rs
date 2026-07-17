// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let mut alt1 = 0;
        for (i, ch) in s.bytes().enumerate() {
            let expected = if i % 2 == 0 { b'0' } else { b'1' };
            if ch != expected {
                alt1 += 1;
            }
        }
        alt1.min(s.len() as i32 - alt1)
    }
}
