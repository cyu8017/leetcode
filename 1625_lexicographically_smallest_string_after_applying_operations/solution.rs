// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn find_lex_smallest_string(s: String, a: i32, b: i32) -> String {
        let mut seen = HashSet::new();
        seen.insert(s.clone());
        let mut q = VecDeque::from([s.clone()]);
        let mut ans = s;
        let b = b as usize;
        while let Some(cur) = q.pop_front() {
            if cur < ans {
                ans = cur.clone();
            }
            let mut bytes = cur.clone().into_bytes();
            for i in (1..bytes.len()).step_by(2) {
                bytes[i] = ((bytes[i] - b'0') as i32 + a) as u8 % 10 + b'0';
            }
            let add = String::from_utf8(bytes).unwrap();
            let n = cur.len();
            let rot = format!("{}{}", &cur[n - b..], &cur[..n - b]);
            for nxt in [add, rot] {
                if seen.insert(nxt.clone()) {
                    q.push_back(nxt);
                }
            }
        }
        ans
    }
}
