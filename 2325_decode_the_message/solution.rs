// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

impl Solution {
    pub fn decode_message(key: String, message: String) -> String {
        let mut mp = [0u8; 26];
        let mut next = b'a';
        for c in key.bytes() {
            if c == b' ' || mp[(c - b'a') as usize] != 0 {
                continue;
            }
            mp[(c - b'a') as usize] = next;
            next += 1;
        }
        message
            .bytes()
            .map(|c| {
                if c == b' ' {
                    ' '
                } else {
                    mp[(c - b'a') as usize] as char
                }
            })
            .collect()
    }
}
