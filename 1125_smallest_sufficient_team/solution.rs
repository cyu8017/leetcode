// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

use std::collections::HashMap;

impl Solution {
    pub fn smallest_sufficient_team(
        req_skills: Vec<String>,
        people: Vec<Vec<String>>,
    ) -> Vec<i32> {
        let mut skill_id = HashMap::new();
        for (i, s) in req_skills.iter().enumerate() {
            skill_id.insert(s.clone(), i);
        }
        let person_masks: Vec<usize> = people
            .iter()
            .map(|skills| {
                let mut mask = 0usize;
                for skill in skills {
                    mask |= 1 << skill_id[skill];
                }
                mask
            })
            .collect();
        let target = (1 << req_skills.len()) - 1;
        let mut dp = vec![i32::MAX; 1 << req_skills.len()];
        let mut choice = vec![0usize; 1 << req_skills.len()];
        let mut prev = vec![0usize; 1 << req_skills.len()];
        dp[0] = 0;
        for state in 0..=target {
            if dp[state] == i32::MAX {
                continue;
            }
            for (i, &mask) in person_masks.iter().enumerate() {
                let ns = state | mask;
                if dp[state] + 1 < dp[ns] {
                    dp[ns] = dp[state] + 1;
                    choice[ns] = i;
                    prev[ns] = state;
                }
            }
        }
        let mut ans = Vec::new();
        let mut state = target;
        while state != 0 {
            ans.push(choice[state] as i32);
            state = prev[state];
        }
        ans
    }
}
