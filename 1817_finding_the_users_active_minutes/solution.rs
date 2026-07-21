// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn finding_users_active_minutes(logs: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut user_minutes: HashMap<i32, HashSet<i32>> = HashMap::new();
        for log in logs {
            user_minutes.entry(log[0]).or_default().insert(log[1]);
        }

        let mut answer = vec![0; k as usize];
        for minutes in user_minutes.values() {
            let uam = minutes.len();
            if uam > 0 && uam <= k as usize {
                answer[uam - 1] += 1;
            }
        }
        answer
    }
}
