// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

use std::collections::HashMap;

impl Solution {
    pub fn better_compression(compressed: String) -> String {
        let b = compressed.as_bytes();
        let n = b.len();
        let mut cnt: HashMap<u8, i32> = HashMap::new();
        let mut i = 0;
        while i < n {
            let c = b[i];
            let mut j = i + 1;
            let mut x = 0i32;
            while j < n && b[j].is_ascii_digit() {
                x = x * 10 + (b[j] - b'0') as i32;
                j += 1;
            }
            *cnt.entry(c).or_insert(0) += x;
            i = j;
        }
        let mut ans = String::new();
        for c in b'a'..=b'z' {
            if let Some(&v) = cnt.get(&c) {
                if v > 0 {
                    ans.push(c as char);
                    ans.push_str(&v.to_string());
                }
            }
        }
        ans
    }
}
