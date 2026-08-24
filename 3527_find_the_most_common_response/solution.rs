// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn find_common_response(responses: Vec<Vec<String>>) -> String {
        let mut cnt: HashMap<String, i32> = HashMap::new();
        for ws in &responses {
            let mut s = HashSet::new();
            for w in ws {
                if s.insert(w.clone()) {
                    *cnt.entry(w.clone()).or_insert(0) += 1;
                }
            }
        }
        let mut ans = responses[0][0].clone();
        let ans_cnt = *cnt.get(&ans).unwrap_or(&0);
        for (w, v) in &cnt {
            let ac = *cnt.get(&ans).unwrap_or(&ans_cnt);
            if ac < *v || (ac == *v && w < &ans) {
                ans = w.clone();
            }
        }
        ans
    }
}
