// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

use std::collections::VecDeque;

impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let mut radiant = VecDeque::new();
        let mut dire = VecDeque::new();
        let n = senate.len() as i32;
        for (i, ch) in senate.chars().enumerate() {
            if ch == 'R' {
                radiant.push_back(i as i32);
            } else {
                dire.push_back(i as i32);
            }
        }
        while !radiant.is_empty() && !dire.is_empty() {
            let r = radiant.pop_front().unwrap();
            let d = dire.pop_front().unwrap();
            if r < d {
                radiant.push_back(r + n);
            } else {
                dire.push_back(d + n);
            }
        }
        if radiant.is_empty() {
            "Dire".to_string()
        } else {
            "Radiant".to_string()
        }
    }
}
