// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

impl Solution {
    pub fn smallest_palindrome(s: String) -> String {
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let mut t = String::new();
        let mut ch = 0u8;
        for c in b'a'..=b'z' {
            let v = cnt[(c - b'a') as usize] / 2;
            t.push_str(&String::from_utf8(vec![c; v as usize]).unwrap());
            cnt[(c - b'a') as usize] -= v * 2;
            if cnt[(c - b'a') as usize] == 1 {
                ch = c;
            }
        }
        let mut sb = t.clone();
        if ch != 0 {
            sb.push(ch as char);
        }
        for c in t.chars().rev() {
            sb.push(c);
        }
        sb
    }
}
