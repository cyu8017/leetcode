// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

impl Solution {
    pub fn vowel_consonant_score(s: String) -> i32 {
        let mut v = 0;
        let mut c = 0;
        for ch in s.bytes() {
            if ch.is_ascii_alphabetic() {
                c += 1;
                if matches!(ch, b'a' | b'e' | b'i' | b'o' | b'u') {
                    v += 1;
                }
            }
        }
        c -= v;
        if c == 0 {
            0
        } else {
            v / c
        }
    }
}
