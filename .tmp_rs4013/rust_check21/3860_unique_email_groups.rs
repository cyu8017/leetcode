struct Solution;
// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

use std::collections::HashSet;

impl Solution {
    pub fn unique_email_groups(emails: Vec<String>) -> i32 {
        let mut st = HashSet::new();
        for email in emails {
            let at = email.find('@').unwrap();
            let mut local = email[..at].to_string();
            let domain = email[at + 1..].to_ascii_lowercase();
            if let Some(plus) = local.find('+') {
                local.truncate(plus);
            }
            let cleaned: String = local
                .chars()
                .filter(|&c| c != '.')
                .map(|c| c.to_ascii_lowercase())
                .collect();
            st.insert(cleaned + &domain);
        }
        st.len() as i32
    }
}
