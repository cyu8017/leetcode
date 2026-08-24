// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

impl Solution {
    pub fn count_vowels(word: String) -> i64 {
        fn is_vowel(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let b = word.as_bytes();
        let n = b.len() as i64;
        let mut ans = 0i64;
        for (i, &c) in b.iter().enumerate() {
            if is_vowel(c) {
                ans += (i as i64 + 1) * (n - i as i64);
            }
        }
        ans
    }
}
