// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        let mut chars: Vec<u8> = s.into_bytes();
        let mut opens = Vec::new();
        for i in 0..chars.len() {
            if chars[i] == b'(' {
                opens.push(i);
            } else if chars[i] == b')' {
                if !opens.is_empty() {
                    opens.pop();
                } else {
                    chars[i] = 0;
                }
            }
        }
        for i in opens {
            chars[i] = 0;
        }
        String::from_utf8(chars.into_iter().filter(|&c| c != 0).collect()).unwrap()
    }
}
