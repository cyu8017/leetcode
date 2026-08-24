// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

use std::collections::HashSet;

impl Solution {
    pub fn match_replacement(s: String, sub: String, mappings: Vec<Vec<char>>) -> bool {
        let mut allow = HashSet::new();
        for m in mappings {
            allow.insert(((m[0] as u32) << 8) | (m[1] as u32));
        }
        let s = s.as_bytes();
        let sub = sub.as_bytes();
        let n = s.len();
        let mlen = sub.len();
        for i in 0..=n.saturating_sub(mlen) {
            let mut ok = true;
            for j in 0..mlen {
                let a = s[i + j] as char;
                let b = sub[j] as char;
                if a == b || allow.contains(&(((b as u32) << 8) | (a as u32))) {
                    continue;
                }
                ok = false;
                break;
            }
            if ok {
                return true;
            }
        }
        false
    }
}
