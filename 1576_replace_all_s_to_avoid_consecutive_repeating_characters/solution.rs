// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

impl Solution {
    pub fn modify_string(s: String) -> String {
        let mut chars: Vec<u8> = s.into_bytes();
        let n = chars.len();
        for i in 0..n {
            if chars[i] == b'?' {
                for c in b'a'..=b'c' {
                    let prev_ok = i == 0 || chars[i - 1] != c;
                    let next_ok = i + 1 == n || chars[i + 1] != c;
                    if prev_ok && next_ok {
                        chars[i] = c;
                        break;
                    }
                }
            }
        }
        String::from_utf8(chars).unwrap()
    }
}
