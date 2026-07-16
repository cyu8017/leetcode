// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

use std::collections::HashMap;

struct TrieNode {
    children: HashMap<u8, TrieNode>,
    is_word: bool,
}

impl TrieNode {
    fn new() -> Self {
        Self {
            children: HashMap::new(),
            is_word: false,
        }
    }
}

pub struct WordDictionary {
    root: TrieNode,
}

impl WordDictionary {
    pub fn new() -> Self {
        Self { root: TrieNode::new() }
    }

    pub fn add_word(&mut self, word: String) {
        let mut node = &mut self.root;
        for byte in word.bytes() {
            node = node.children.entry(byte).or_insert_with(TrieNode::new);
        }
        node.is_word = true;
    }

    pub fn search(&self, word: String) -> bool {
        fn dfs(node: &TrieNode, word: &[u8], index: usize) -> bool {
            if index == word.len() {
                return node.is_word;
            }
            let c = word[index];
            if c == b'.' {
                return node.children.values().any(|child| dfs(child, word, index + 1));
            }
            match node.children.get(&c) {
                Some(next) => dfs(next, word, index + 1),
                None => false,
            }
        }
        dfs(&self.root, word.as_bytes(), 0)
    }
}
