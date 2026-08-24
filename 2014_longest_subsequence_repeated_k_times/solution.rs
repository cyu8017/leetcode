// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

use std::collections::VecDeque;

impl Solution {
    pub fn longest_subsequence_repeated_k(s: String, k: i32) -> String {
        let bytes = s.as_bytes();
        let mut freq = [0i32; 26];
        for &c in bytes {
            freq[(c - b'a') as usize] += 1;
        }
        let mut chars = Vec::new();
        for c in (0..26).rev() {
            if freq[c] >= k {
                chars.push(b'a' + c as u8);
            }
        }
        let is_subseq = |t: &[u8]| -> bool {
            let mut need = 0;
            let mut times = 0;
            for &c in bytes {
                if c == t[need] {
                    need += 1;
                    if need == t.len() {
                        times += 1;
                        if times == k {
                            return true;
                        }
                        need = 0;
                    }
                }
            }
            false
        };
        let mut best = String::new();
        let mut q = VecDeque::new();
        q.push_back(Vec::new());
        while let Some(cur) = q.pop_front() {
            for &ch in &chars {
                let mut nxt = cur.clone();
                nxt.push(ch);
                if is_subseq(&nxt) {
                    let cand = String::from_utf8(nxt.clone()).unwrap();
                    if cand.len() > best.len() || (cand.len() == best.len() && cand > best) {
                        best = cand;
                    }
                    q.push_back(nxt);
                }
            }
        }
        best
    }
}
