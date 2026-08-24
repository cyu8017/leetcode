struct Solution;
// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

impl Solution {
    pub fn sum_prefix_scores(words: Vec<String>) -> Vec<i32> {
        struct TrieNode {
            child: [Option<Box<TrieNode>>; 26],
            cnt: i32,
        }
        impl TrieNode {
            fn new() -> Self {
                Self {
                    child: Default::default(),
                    cnt: 0,
                }
            }
        }
        let mut root = TrieNode::new();
        for w in &words {
            let mut cur = &mut root;
            for &ch in w.as_bytes() {
                let c = (ch - b'a') as usize;
                if cur.child[c].is_none() {
                    cur.child[c] = Some(Box::new(TrieNode::new()));
                }
                cur = cur.child[c].as_mut().unwrap();
                cur.cnt += 1;
            }
        }
        let mut ans = vec![0; words.len()];
        for (i, w) in words.iter().enumerate() {
            let mut cur = &root;
            let mut sum = 0;
            for &ch in w.as_bytes() {
                cur = cur.child[(ch - b'a') as usize].as_ref().unwrap();
                sum += cur.cnt;
            }
            ans[i] = sum;
        }
        ans
    }
}

fn main() {}
