struct Solution;
// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

use std::collections::HashSet;

impl Solution {
    pub fn report_spam(message: Vec<String>, banned_words: Vec<String>) -> bool {
        let ban: HashSet<String> = banned_words.into_iter().collect();
        let mut cnt = 0;
        for w in message {
            if ban.contains(&w) {
                cnt += 1;
                if cnt >= 2 {
                    return true;
                }
            }
        }
        false
    }
}

fn main() {}
