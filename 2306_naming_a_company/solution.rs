// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

use std::collections::HashSet;

impl Solution {
    pub fn distinct_names(ideas: Vec<String>) -> i64 {
        let mut groups: Vec<HashSet<String>> = vec![HashSet::new(); 26];
        for idea in ideas {
            let b = idea.as_bytes();
            groups[(b[0] - b'a') as usize].insert(idea[1..].to_string());
        }
        let mut ans = 0i64;
        for i in 0..26 {
            for j in i + 1..26 {
                let overlap = groups[i].iter().filter(|s| groups[j].contains(*s)).count() as i64;
                ans += (groups[i].len() as i64 - overlap) * (groups[j].len() as i64 - overlap) * 2;
            }
        }
        ans
    }
}
