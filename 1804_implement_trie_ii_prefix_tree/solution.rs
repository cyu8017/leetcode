// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

pub struct Trie {
    children: [Option<Box<Trie>>; 26],
    word_count: i32,
    prefix_count: i32,
}

impl Trie {
    pub fn new() -> Self {
        Self {
            children: std::array::from_fn(|_| None),
            word_count: 0,
            prefix_count: 0,
        }
    }

    pub fn insert(&mut self, word: String) {
        let mut node = self;
        for byte in word.bytes() {
            let idx = (byte - b'a') as usize;
            node = node.children[idx].get_or_insert_with(|| Box::new(Trie::new()));
            node.prefix_count += 1;
        }
        node.word_count += 1;
    }

    fn find(&self, text: &str) -> Option<&Trie> {
        let mut node = self;
        for byte in text.bytes() {
            node = node.children[(byte - b'a') as usize].as_deref()?;
        }
        Some(node)
    }

    pub fn count_words_equal_to(&self, word: String) -> i32 {
        self.find(&word).map_or(0, |node| node.word_count)
    }

    pub fn count_words_starting_with(&self, prefix: String) -> i32 {
        self.find(&prefix).map_or(0, |node| node.prefix_count)
    }

    pub fn erase(&mut self, word: String) {
        let mut node = self;
        for byte in word.bytes() {
            node = node.children[(byte - b'a') as usize].as_mut().unwrap();
            node.prefix_count -= 1;
        }
        node.word_count -= 1;
    }
}
