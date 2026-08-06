// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn most_visited_pattern(
        username: Vec<String>,
        timestamp: Vec<i32>,
        website: Vec<String>,
    ) -> Vec<String> {
        let mut visits: HashMap<String, Vec<(i32, String)>> = HashMap::new();
        for i in 0..username.len() {
            visits
                .entry(username[i].clone())
                .or_default()
                .push((timestamp[i], website[i].clone()));
        }
        let mut scores: HashMap<(String, String, String), i32> = HashMap::new();
        for vs in visits.values_mut() {
            vs.sort_by_key(|v| v.0);
            let sites: Vec<&str> = vs.iter().map(|v| v.1.as_str()).collect();
            let mut patterns = HashSet::new();
            for i in 0..sites.len() {
                for j in i + 1..sites.len() {
                    for k in j + 1..sites.len() {
                        patterns.insert((
                            sites[i].to_string(),
                            sites[j].to_string(),
                            sites[k].to_string(),
                        ));
                    }
                }
            }
            for p in patterns {
                *scores.entry(p).or_insert(0) += 1;
            }
        }
        let mut best: Option<(String, String, String)> = None;
        let mut best_count = -1;
        for (p, c) in scores {
            if c > best_count || (c == best_count && (best.is_none() || Some(&p) < best.as_ref())) {
                best = Some(p);
                best_count = c;
            }
        }
        let best = best.unwrap();
        vec![best.0, best.1, best.2]
    }
}
