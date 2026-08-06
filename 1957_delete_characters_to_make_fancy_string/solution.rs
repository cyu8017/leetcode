// LeetCode 1957 - Delete Characters to Make Fancy String
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

impl Solution {
    pub fn make_fancy_string(s: String) -> String {
        let mut ans = String::new();
        for c in s.chars() {
            let bytes = ans.as_bytes();
            if bytes.len() >= 2
                && bytes[bytes.len() - 1] == c as u8
                && bytes[bytes.len() - 2] == c as u8
            {
                continue;
            }
            ans.push(c);
        }
        ans
    }
}
