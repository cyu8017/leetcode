// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

use std::collections::HashMap;

impl Solution {
    pub fn is_scramble(s1: String, s2: String) -> bool {
        let mut memo = HashMap::new();
        Self::dfs(&s1, &s2, &mut memo)
    }

    fn dfs(a: &str, b: &str, memo: &mut HashMap<String, bool>) -> bool {
        let key = format!("{}#{}", a, b);
        if let Some(&v) = memo.get(&key) {
            return v;
        }
        if a == b {
            memo.insert(key, true);
            return true;
        }
        let mut sa: Vec<char> = a.chars().collect();
        let mut sb: Vec<char> = b.chars().collect();
        sa.sort_unstable();
        sb.sort_unstable();
        if sa != sb {
            memo.insert(key, false);
            return false;
        }

        let n = a.len();
        for i in 1..n {
            if Self::dfs(&a[..i], &b[..i], memo) && Self::dfs(&a[i..], &b[i..], memo) {
                memo.insert(key, true);
                return true;
            }
            if Self::dfs(&a[..i], &b[n - i..], memo) && Self::dfs(&a[i..], &b[..n - i], memo) {
                memo.insert(key, true);
                return true;
            }
        }
        memo.insert(key, false);
        false
    }
}
