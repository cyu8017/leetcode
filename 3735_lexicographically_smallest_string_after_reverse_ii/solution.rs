// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

impl Solution {
    pub fn lex_smallest(s: String) -> String {
        let n = s.len();
        let bytes = s.as_bytes();
        let mut best = s.clone();
        for i in 1..=n {
            let mut t = bytes.to_vec();
            t[..i].reverse();
            let t = String::from_utf8(t).unwrap();
            if t < best {
                best = t;
            }
        }
        for i in 0..n {
            let mut t = bytes.to_vec();
            t[i..].reverse();
            let t = String::from_utf8(t).unwrap();
            if t < best {
                best = t;
            }
        }
        best
    }
}
