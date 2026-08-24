// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

impl Solution {
    pub fn decode_ciphertext(encoded_text: String, rows: i32) -> String {
        if rows == 1 {
            return encoded_text;
        }
        let rows = rows as usize;
        let cols = encoded_text.len() / rows;
        let b = encoded_text.as_bytes();
        let mut out = Vec::new();
        for c in 0..cols {
            let mut r = 0;
            while r < rows && c + r < cols {
                out.push(b[r * cols + c + r]);
                r += 1;
            }
        }
        while out.last() == Some(&b' ') {
            out.pop();
        }
        String::from_utf8(out).unwrap()
    }
}
