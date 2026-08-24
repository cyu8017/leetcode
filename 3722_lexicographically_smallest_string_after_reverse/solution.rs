// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

impl Solution {
    pub fn lex_smallest(s: String) -> String {
        let n = s.len();
        let bytes = s.as_bytes();
        let mut ans = s.clone();
        for k in 1..=n {
            let mut t1 = bytes[..k].to_vec();
            t1.reverse();
            t1.extend_from_slice(&bytes[k..]);
            let t1 = String::from_utf8(t1).unwrap();
            let mut t2 = bytes[..n - k].to_vec();
            let mut suf = bytes[n - k..].to_vec();
            suf.reverse();
            t2.extend(suf);
            let t2 = String::from_utf8(t2).unwrap();
            ans = ans.min(t1).min(t2);
        }
        ans
    }
}
