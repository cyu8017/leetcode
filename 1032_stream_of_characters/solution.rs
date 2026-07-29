// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

use std::collections::HashMap;

#[derive(Default)]
struct TrieNode {
    children: HashMap<char, TrieNode>,
    end: bool,
}

pub struct StreamChecker {
    trie: TrieNode,
    stream: Vec<char>,
}

impl StreamChecker {
    pub fn new(words: Vec<String>) -> Self {
        let mut trie = TrieNode::default();
        for word in words {
            let mut node = &mut trie;
            for ch in word.chars().rev() {
                node = node.children.entry(ch).or_default();
            }
            node.end = true;
        }
        Self {
            trie,
            stream: Vec::new(),
        }
    }

    pub fn query(&mut self, letter: char) -> bool {
        self.stream.push(letter);
        let mut node = &self.trie;
        for &ch in self.stream.iter().rev() {
            if node.end {
                return true;
            }
            match node.children.get(&ch) {
                Some(next) => node = next,
                None => return false,
            }
        }
        node.end
    }
}
