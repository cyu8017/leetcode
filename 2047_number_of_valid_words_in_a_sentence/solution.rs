// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

impl Solution {
    pub fn count_valid_words(sentence: String) -> i32 {
        fn valid(w: &str) -> bool {
            if w.is_empty() {
                return false;
            }
            let b = w.as_bytes();
            let mut hyphen = 0;
            for i in 0..b.len() {
                let c = b[i];
                if c.is_ascii_digit() {
                    return false;
                }
                if c == b'-' {
                    hyphen += 1;
                    if hyphen > 1 || i == 0 || i == b.len() - 1 {
                        return false;
                    }
                    if !b[i - 1].is_ascii_lowercase() || !b[i + 1].is_ascii_lowercase() {
                        return false;
                    }
                } else if c == b'!' || c == b'.' || c == b',' {
                    if i != b.len() - 1 {
                        return false;
                    }
                } else if !c.is_ascii_lowercase() {
                    return false;
                }
            }
            true
        }
        sentence.split_whitespace().filter(|w| valid(w)).count() as i32
    }
}
