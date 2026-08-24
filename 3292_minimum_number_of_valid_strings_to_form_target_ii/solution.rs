// LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

struct TrieNode {
    next: [Option<Box<TrieNode>>; 26],
}

impl TrieNode {
    fn new() -> Self {
        Self {
            next: Default::default(),
        }
    }
}

impl Solution {
    pub fn min_valid_strings(words: Vec<String>, target: String) -> i32 {
        let n = target.len();
        const INF: i32 = 1_000_000_000;
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        let mut root = TrieNode::new();
        for w in &words {
            let mut cur = &mut root;
            for c in w.bytes() {
                let ci = (c - b'a') as usize;
                if cur.next[ci].is_none() {
                    cur.next[ci] = Some(Box::new(TrieNode::new()));
                }
                cur = cur.next[ci].as_mut().unwrap();
            }
        }
        let tb = target.as_bytes();
        for i in 0..n {
            if dp[i] == INF {
                continue;
            }
            let mut cur = &root;
            for j in i..n {
                let ci = (tb[j] - b'a') as usize;
                if cur.next[ci].is_none() {
                    break;
                }
                cur = cur.next[ci].as_ref().unwrap();
                if dp[i] + 1 < dp[j + 1] {
                    dp[j + 1] = dp[i] + 1;
                }
            }
        }
        if dp[n] == INF { -1 } else { dp[n] }
    }
}
