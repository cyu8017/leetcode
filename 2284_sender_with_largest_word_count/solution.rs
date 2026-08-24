// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

use std::collections::HashMap;

impl Solution {
    pub fn largest_word_count(messages: Vec<String>, senders: Vec<String>) -> String {
        let mut count = HashMap::new();
        let mut best = String::new();
        let mut best_cnt = -1;
        for i in 0..messages.len() {
            let words = 1 + messages[i].bytes().filter(|&c| c == b' ').count() as i32;
            let c = count.entry(senders[i].clone()).or_insert(0);
            *c += words;
            let c = *c;
            if c > best_cnt || (c == best_cnt && senders[i] > best) {
                best_cnt = c;
                best = senders[i].clone();
            }
        }
        best
    }
}
