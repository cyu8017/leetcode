// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

pub struct MagicDictionary {
    words: Vec<String>,
}

impl MagicDictionary {
    pub fn new() -> Self {
        Self { words: Vec::new() }
    }

    pub fn build_dict(&mut self, dictionary: Vec<String>) {
        self.words = dictionary;
    }

    pub fn search(&self, search_word: String) -> bool {
        for word in &self.words {
            if word.len() != search_word.len() {
                continue;
            }
            let diff = word
                .bytes()
                .zip(search_word.bytes())
                .filter(|(a, b)| a != b)
                .count();
            if diff == 1 {
                return true;
            }
        }
        false
    }
}
