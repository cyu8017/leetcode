// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

struct Trie {
    children: [Option<Box<Trie>>; 26],
    length: i32,
    idx: i32,
}

impl Trie {
    fn new() -> Self {
        const INF: i32 = 1 << 30;
        Self {
            children: Default::default(),
            length: INF,
            idx: INF,
        }
    }

    fn insert(&mut self, w: &[u8], i: i32) {
        let mut node = self;
        if node.length > w.len() as i32 {
            node.length = w.len() as i32;
            node.idx = i;
        }
        for k in (0..w.len()).rev() {
            let id = (w[k] - b'a') as usize;
            node = node.children[id].get_or_insert_with(|| Box::new(Trie::new()));
            if node.length > w.len() as i32 {
                node.length = w.len() as i32;
                node.idx = i;
            }
        }
    }

    fn query(&self, w: &[u8]) -> i32 {
        let mut node = self;
        for k in (0..w.len()).rev() {
            let id = (w[k] - b'a') as usize;
            match &node.children[id] {
                Some(child) => node = child,
                None => break,
            }
        }
        node.idx
    }
}

impl Solution {
    pub fn string_indices(words_container: Vec<String>, words_query: Vec<String>) -> Vec<i32> {
        let mut trie = Trie::new();
        for (i, w) in words_container.iter().enumerate() {
            trie.insert(w.as_bytes(), i as i32);
        }
        words_query.iter().map(|w| trie.query(w.as_bytes())).collect()
    }
}
