// LeetCode 1309 - Decrypt String from Alphabet to Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

impl Solution {
    pub fn freq_alphabets(s: String) -> String {
        let bytes = s.as_bytes();
        let mut answer = Vec::new();
        let mut i = bytes.len() as i32 - 1;
        while i >= 0 {
            if bytes[i as usize] == b'#' {
                let num = (bytes[(i - 2) as usize] - b'0') as i32 * 10
                    + (bytes[(i - 1) as usize] - b'0') as i32;
                answer.push((b'a' + (num - 1) as u8) as char);
                i -= 3;
            } else {
                answer.push((b'a' + bytes[i as usize] - b'0' - 1) as char);
                i -= 1;
            }
        }
        answer.reverse();
        answer.into_iter().collect()
    }
}
