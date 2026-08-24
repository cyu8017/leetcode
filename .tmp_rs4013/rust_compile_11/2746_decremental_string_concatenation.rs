struct Solution;
fn main() {}

// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

use std::collections::HashMap;

impl Solution {
    pub fn minimize_concatenated_length(words: Vec<String>) -> i32 {
        let n = words.len();
        let mut memo: HashMap<(usize, u8, u8), i32> = HashMap::new();
        fn dfs(
            i: usize,
            first: u8,
            last: u8,
            words: &[String],
            memo: &mut HashMap<(usize, u8, u8), i32>,
        ) -> i32 {
            if i == words.len() {
                return 0;
            }
            if let Some(&v) = memo.get(&(i, first, last)) {
                return v;
            }
            let w = words[i].as_bytes();
            let wf = w[0];
            let wl = w[w.len() - 1];
            let add1 = w.len() as i32 - if last == wf { 1 } else { 0 };
            let add2 = w.len() as i32 - if wl == first { 1 } else { 0 };
            let a = add1 + dfs(i + 1, first, wl, words, memo);
            let b = add2 + dfs(i + 1, wf, last, words, memo);
            let res = a.min(b);
            memo.insert((i, first, last), res);
            res
        }
        let w0 = words[0].as_bytes();
        w0.len() as i32 + dfs(1, w0[0], w0[w0.len() - 1], &words, &mut memo)
    }
}
