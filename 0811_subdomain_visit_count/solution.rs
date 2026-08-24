// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

use std::collections::HashMap;

impl Solution {
    pub fn subdomain_visits(cpdomains: Vec<String>) -> Vec<String> {
        let mut counts = HashMap::new();
        for item in &cpdomains {
            let space = item.find(' ').unwrap();
            let count: i32 = item[..space].parse().unwrap();
            let mut domain = &item[space + 1..];
            loop {
                *counts.entry(domain.to_string()).or_insert(0) += count;
                if let Some(dot) = domain.find('.') {
                    domain = &domain[dot + 1..];
                } else {
                    break;
                }
            }
        }
        counts
            .into_iter()
            .map(|(domain, count)| format!("{count} {domain}"))
            .collect()
    }
}
