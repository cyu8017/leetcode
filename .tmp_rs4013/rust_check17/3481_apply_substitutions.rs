struct Solution;
// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

use std::collections::HashMap;

impl Solution {
    pub fn apply_substitutions(replacements: Vec<Vec<String>>, text: String) -> String {
        let mut mp = HashMap::new();
        for r in replacements {
            mp.insert(r[0].clone(), r[1].clone());
        }
        fn resolve(s: &str, mp: &HashMap<String, String>) -> String {
            let bytes = s.as_bytes();
            let mut out = String::new();
            let mut i = 0;
            while i < bytes.len() {
                if bytes[i] == b'%' {
                    let mut j = i + 1;
                    while j < bytes.len() && bytes[j] != b'%' {
                        j += 1;
                    }
                    let key = &s[i + 1..j];
                    let val = mp.get(key).map(|v| v.as_str()).unwrap_or("");
                    out.push_str(&resolve(val, mp));
                    i = j + 1;
                } else {
                    out.push(bytes[i] as char);
                    i += 1;
                }
            }
            out
        }
        resolve(&text, &mp)
    }
}

fn main() {}
