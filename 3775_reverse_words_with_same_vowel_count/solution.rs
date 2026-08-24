// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

impl Solution {
    fn calc(w: &str) -> i32 {
        w.bytes()
            .filter(|&c| matches!(c, b'a' | b'e' | b'i' | b'o' | b'u'))
            .count() as i32
    }

    pub fn reverse_words(s: String) -> String {
        let words: Vec<&str> = s.split_whitespace().collect();
        if words.is_empty() {
            return String::new();
        }
        let cnt = Self::calc(words[0]);
        let mut ans = Vec::new();
        ans.push(words[0].to_string());
        for w in words.iter().skip(1) {
            let mut w = w.to_string();
            if Self::calc(&w) == cnt {
                let mut bytes = w.into_bytes();
                bytes.reverse();
                w = String::from_utf8(bytes).unwrap();
            }
            ans.push(w);
        }
        ans.join(" ")
    }
}
