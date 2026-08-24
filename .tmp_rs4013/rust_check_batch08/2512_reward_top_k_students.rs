struct Solution;
// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

use std::collections::HashSet;

impl Solution {
    pub fn top_students(
        positive_feedback: Vec<String>,
        negative_feedback: Vec<String>,
        report: Vec<String>,
        student_id: Vec<i32>,
        k: i32,
    ) -> Vec<i32> {
        let pos: HashSet<&str> = positive_feedback.iter().map(|s| s.as_str()).collect();
        let neg: HashSet<&str> = negative_feedback.iter().map(|s| s.as_str()).collect();
        let mut arr: Vec<(i32, i32)> = Vec::new();
        for i in 0..report.len() {
            let mut score = 0;
            for w in report[i].split_whitespace() {
                if pos.contains(w) {
                    score += 3;
                } else if neg.contains(w) {
                    score -= 1;
                }
            }
            arr.push((student_id[i], score));
        }
        arr.sort_by(|a, b| {
            if a.1 != b.1 {
                b.1.cmp(&a.1)
            } else {
                a.0.cmp(&b.0)
            }
        });
        arr.into_iter().take(k as usize).map(|(id, _)| id).collect()
    }
}

fn main() {}
