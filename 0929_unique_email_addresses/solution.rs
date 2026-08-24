// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

use std::collections::HashSet;

impl Solution {
    pub fn num_unique_emails(emails: Vec<String>) -> i32 {
        let mut normalized = HashSet::new();
        for email in emails {
            let at = email.find('@').unwrap();
            let mut local = email[..at].to_string();
            let domain = email[at..].to_string();
            if let Some(plus) = local.find('+') {
                local.truncate(plus);
            }
            let cleaned: String = local.chars().filter(|&c| c != '.').collect();
            normalized.insert(cleaned + &domain);
        }
        normalized.len() as i32
    }
}
