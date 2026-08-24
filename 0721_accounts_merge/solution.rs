// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

use std::collections::HashMap;

impl Solution {
    pub fn accounts_merge(accounts: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let mut parent = HashMap::new();
        let mut email_name = HashMap::new();

        for account in &accounts {
            let name = &account[0];
            let first = &account[1];
            for email in account.iter().skip(1) {
                parent.entry(email.clone()).or_insert_with(|| email.clone());
                email_name.insert(email.clone(), name.clone());
                let pa = Self::find(&mut parent, first);
                let pb = Self::find(&mut parent, email);
                parent.insert(pa, pb);
            }
        }

        let mut groups: HashMap<String, Vec<String>> = HashMap::new();
        let emails: Vec<String> = parent.keys().cloned().collect();
        for email in emails {
            let root = Self::find(&mut parent, &email);
            groups.entry(root).or_default().push(email);
        }

        let mut result = Vec::new();
        for emails in groups.into_values() {
            let mut emails = emails;
            emails.sort();
            let mut row = vec![email_name[&emails[0]].clone()];
            row.extend(emails);
            result.push(row);
        }
        result
    }

    fn find(parent: &mut HashMap<String, String>, x: &str) -> String {
        let mut cur = x.to_string();
        while parent[&cur] != cur {
            let grand = parent[&parent[&cur]].clone();
            parent.insert(cur.clone(), grand);
            cur = parent[&cur].clone();
        }
        cur
    }
}
