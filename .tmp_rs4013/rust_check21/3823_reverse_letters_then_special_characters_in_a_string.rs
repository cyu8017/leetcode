struct Solution;
// LeetCode 3823 - Reverse Letters Then Special Characters in a String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

impl Solution {
    pub fn reverse_by_type(s: String) -> String {
        let mut bytes = s.into_bytes();
        let mut a = Vec::new();
        let mut b = Vec::new();
        for &c in &bytes {
            if c.is_ascii_alphabetic() {
                a.push(c);
            } else {
                b.push(c);
            }
        }
        let mut j = a.len();
        let mut k = b.len();
        for c in &mut bytes {
            if c.is_ascii_alphabetic() {
                j -= 1;
                *c = a[j];
            } else {
                k -= 1;
                *c = b[k];
            }
        }
        String::from_utf8(bytes).unwrap()
    }
}
