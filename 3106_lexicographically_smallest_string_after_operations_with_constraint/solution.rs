// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

impl Solution {
    pub fn get_smallest_string(s: String, mut k: i32) -> String {
        let mut s = s.into_bytes();
        for i in 0..s.len() {
            let c1 = s[i];
            for c2 in b'a'..c1 {
                let d = (c1 - c2).min(26 - (c1 - c2)) as i32;
                if d <= k {
                    s[i] = c2;
                    k -= d;
                    break;
                }
            }
        }
        String::from_utf8(s).unwrap()
    }
}
