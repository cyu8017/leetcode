// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

use std::collections::{HashMap, HashSet};

struct TrieNode {
    children: HashMap<u8, TrieNode>,
    word: Option<String>,
}

impl TrieNode {
    fn new() -> Self {
        Self {
            children: HashMap::new(),
            word: None,
        }
    }
}

impl Solution {
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let mut root = TrieNode::new();
        for word in words {
            let mut node = &mut root;
            for byte in word.bytes() {
                node = node.children.entry(byte).or_insert_with(TrieNode::new);
            }
            node.word = Some(word);
        }

        let rows = board.len();
        let cols = board[0].len();
        let mut board = board;
        let mut result = HashSet::new();

        fn dfs(
            board: &mut Vec<Vec<char>>,
            row: usize,
            col: usize,
            node: &mut TrieNode,
            result: &mut HashSet<String>,
        ) {
            let c = board[row][col] as u8;
            let next = match node.children.get_mut(&c) {
                Some(child) => child,
                None => return,
            };
            if let Some(word) = next.word.take() {
                result.insert(word);
            }
            board[row][col] = '#';
            if row + 1 < board.len() && board[row + 1][col] != '#' {
                dfs(board, row + 1, col, next, result);
            }
            if row > 0 && board[row - 1][col] != '#' {
                dfs(board, row - 1, col, next, result);
            }
            if col + 1 < board[0].len() && board[row][col + 1] != '#' {
                dfs(board, row, col + 1, next, result);
            }
            if col > 0 && board[row][col - 1] != '#' {
                dfs(board, row, col - 1, next, result);
            }
            board[row][col] = c as char;
            if next.children.is_empty() {
                node.children.remove(&c);
            }
        }

        for row in 0..rows {
            for col in 0..cols {
                dfs(&mut board, row, col, &mut root, &mut result);
            }
        }
        result.into_iter().collect()
    }
}
