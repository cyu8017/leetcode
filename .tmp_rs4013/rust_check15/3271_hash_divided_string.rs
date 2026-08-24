struct Solution;
// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

impl Solution {
    pub fn string_hash(s: String, k: i32) -> String {
        let b = s.as_bytes();
        let k = k as usize;
        let mut out = String::new();
        let mut i = 0;
        while i < b.len() {
            let mut sum = 0;
            for j in i..i + k {
                sum += (b[j] - b'a') as i32;
            }
            out.push(char::from(b'a' + (sum % 26) as u8));
            i += k;
        }
        out
    }
}

fn main() {}
