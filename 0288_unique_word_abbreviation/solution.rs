// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

use std::collections::{HashMap, HashSet};

struct ValidWordAbbr {
    groups: HashMap<String, HashSet<String>>,
}

impl ValidWordAbbr {
    fn new(dictionary: Vec<String>) -> Self {
        let mut groups = HashMap::new();
        for word in dictionary {
            let key = Self::abbreviate(&word);
            groups.entry(key).or_insert_with(HashSet::new).insert(word);
        }
        Self { groups }
    }

    fn is_unique(&self, word: String) -> bool {
        let key = Self::abbreviate(&word);
        match self.groups.get(&key) {
            None => true,
            Some(words) => words.len() == 1 && words.contains(&word),
        }
    }

    fn abbreviate(word: &str) -> String {
        if word.len() <= 2 {
            return word.to_string();
        }
        format!("{}{}{}", word.as_bytes()[0], word.len() - 2, word.as_bytes()[word.len() - 1] as char)
    }
}
