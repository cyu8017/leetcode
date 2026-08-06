// LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let s = s.as_bytes();
        let k = k as usize;
        let is_vowel = |c: u8| matches!(c, b'a' | b'e' | b'i' | b'o' | b'u');
        let mut cur = s[..k].iter().filter(|&&c| is_vowel(c)).count() as i32;
        let mut ans = cur;
        for i in k..s.len() {
            cur += i32::from(is_vowel(s[i])) - i32::from(is_vowel(s[i - k]));
            ans = ans.max(cur);
        }
        ans
    }
}
