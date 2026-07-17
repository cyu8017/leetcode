// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

use std::collections::HashSet;

impl Solution {
    pub fn minimum_teachings(n: i32, languages: Vec<Vec<i32>>, friendships: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let users = languages.len();
        let mut knows = vec![vec![false; n + 1]; users];
        for user in 0..users {
            for &lang in &languages[user] {
                knows[user][lang as usize] = true;
            }
        }
        let mut need: HashSet<usize> = HashSet::new();
        for friendship in &friendships {
            let u = friendship[0] as usize - 1;
            let v = friendship[1] as usize - 1;
            let shares = languages[u].iter().any(|&lang| knows[v][lang as usize]);
            if !shares {
                need.insert(u);
                need.insert(v);
            }
        }
        if need.is_empty() {
            return 0;
        }
        (1..=n)
            .map(|lang| need.iter().filter(|&&user| !knows[user][lang]).count())
            .min()
            .unwrap() as i32
    }
}
