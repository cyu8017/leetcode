// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

use std::collections::HashMap;

impl Solution {
    pub fn longest_wpi(hours: Vec<i32>) -> i32 {
        let mut score = 0;
        let mut first_seen = HashMap::new();
        first_seen.insert(0, -1);
        let mut ans = 0;
        for (i, &h) in hours.iter().enumerate() {
            score += if h > 8 { 1 } else { -1 };
            if score > 0 {
                ans = i as i32 + 1;
            } else if let Some(&j) = first_seen.get(&(score - 1)) {
                ans = ans.max(i as i32 - j);
            }
            first_seen.entry(score).or_insert(i as i32);
        }
        ans
    }
}
