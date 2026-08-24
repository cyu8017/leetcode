// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

impl Solution {
    pub fn beautiful_substrings(s: String, k: i32) -> i32 {
        fn is_vowel(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let s = s.as_bytes();
        let n = s.len();
        let mut ans = 0;
        for i in 0..n {
            let mut v = 0;
            let mut c = 0;
            for j in i..n {
                if is_vowel(s[j]) {
                    v += 1;
                } else {
                    c += 1;
                }
                if v == c && (v * c) % k == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
