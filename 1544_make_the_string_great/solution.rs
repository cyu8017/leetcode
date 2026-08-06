// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

impl Solution {
    pub fn make_good(s: String) -> String {
        let mut stack: Vec<u8> = Vec::new();
        for ch in s.bytes() {
            if let Some(&top) = stack.last() {
                if top != ch && top.to_ascii_lowercase() == ch.to_ascii_lowercase() {
                    stack.pop();
                    continue;
                }
            }
            stack.push(ch);
        }
        String::from_utf8(stack).unwrap()
    }
}
