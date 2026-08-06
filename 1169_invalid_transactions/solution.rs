// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

use std::collections::HashSet;

impl Solution {
    pub fn invalid_transactions(transactions: Vec<String>) -> Vec<String> {
        #[derive(Clone)]
        struct Tx {
            name: String,
            city: String,
            raw: String,
            time: i32,
            amount: i32,
        }
        let parsed: Vec<Tx> = transactions
            .iter()
            .map(|t| {
                let parts: Vec<&str> = t.split(',').collect();
                Tx {
                    name: parts[0].to_string(),
                    city: parts[3].to_string(),
                    raw: t.clone(),
                    time: parts[1].parse().unwrap(),
                    amount: parts[2].parse().unwrap(),
                }
            })
            .collect();
        let mut invalid = HashSet::new();
        for i in 0..parsed.len() {
            let a = &parsed[i];
            if a.amount > 1000 {
                invalid.insert(a.raw.clone());
            }
            for j in 0..parsed.len() {
                if i == j {
                    continue;
                }
                let b = &parsed[j];
                if a.name == b.name && a.city != b.city && (a.time - b.time).abs() <= 60 {
                    invalid.insert(a.raw.clone());
                    invalid.insert(b.raw.clone());
                }
            }
        }
        transactions.into_iter().filter(|t| invalid.contains(t)).collect()
    }
}
