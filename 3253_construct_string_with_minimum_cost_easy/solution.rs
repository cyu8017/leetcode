// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_cost(target: String, words: Vec<String>, costs: Vec<i32>) -> i32 {
        const INF: i64 = 1_000_000_000_000_000_000;
        let n = target.len();
        let tb = target.as_bytes();
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        let mut best: HashMap<String, i32> = HashMap::new();
        for (i, w) in words.iter().enumerate() {
            let e = best.entry(w.clone()).or_insert(i32::MAX);
            if costs[i] < *e {
                *e = costs[i];
            }
        }
        for i in 0..n {
            if dp[i] == INF {
                continue;
            }
            for (w, &c) in &best {
                let l = w.len();
                if i + l <= n && &tb[i..i + l] == w.as_bytes() && dp[i] + (c as i64) < dp[i + l] {
                    dp[i + l] = dp[i] + c as i64;
                }
            }
        }
        if dp[n] == INF { -1 } else { dp[n] as i32 }
    }
}
