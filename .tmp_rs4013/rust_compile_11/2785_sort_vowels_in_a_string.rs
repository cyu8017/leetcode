struct Solution;
fn main() {}

// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

impl Solution {
    pub fn sort_vowels(s: String) -> String {
        fn is_vowel(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u' | b'A' | b'E' | b'I' | b'O' | b'U')
        }
        let mut b = s.into_bytes();
        let mut vowels: Vec<u8> = b.iter().copied().filter(|&c| is_vowel(c)).collect();
        vowels.sort_unstable();
        let mut vi = 0;
        for c in &mut b {
            if is_vowel(*c) {
                *c = vowels[vi];
                vi += 1;
            }
        }
        String::from_utf8(b).unwrap()
    }
}
