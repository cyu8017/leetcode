struct Solution;
// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

impl Solution {
    pub fn get_encrypted_string(s: String, k: i32) -> String {
        let n = s.len();
        let b = s.as_bytes();
        let mut cs = vec![0u8; n];
        for i in 0..n {
            cs[i] = b[(i + k as usize) % n];
        }
        String::from_utf8(cs).unwrap()
    }
}

fn main() {}
