#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn minimum_cost(
        source: String,
        target: String,
        original: Vec<String>,
        changed: Vec<String>,
        cost: Vec<i32>,
    ) -> i64 {
        const INF: i64 = 1i64 << 60;
        let mut ids: HashMap<String, usize> = HashMap::new();
        let mut next_id = 0usize;
        let mut get_id = |s: &str, ids: &mut HashMap<String, usize>, next_id: &mut usize| -> usize {
            if let Some(&v) = ids.get(s) {
                return v;
            }
            let v = *next_id;
            ids.insert(s.to_string(), v);
            *next_id += 1;
            v
        };
        for i in 0..original.len() {
            get_id(&original[i], &mut ids, &mut next_id);
            get_id(&changed[i], &mut ids, &mut next_id);
        }
        let m = ids.len();
        let mut dist = vec![vec![INF; m]; m];
        for i in 0..m {
            dist[i][i] = 0;
        }
        for i in 0..original.len() {
            let u = *ids.get(&original[i]).unwrap();
            let v = *ids.get(&changed[i]).unwrap();
            let ww = cost[i] as i64;
            if ww < dist[u][v] {
                dist[u][v] = ww;
            }
        }
        for k in 0..m {
            for i in 0..m {
                for j in 0..m {
                    if dist[i][k] + dist[k][j] < dist[i][j] {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        let n = source.len();
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        let lens: HashSet<usize> = ids.keys().map(|s| s.len()).collect();
        let src = source.as_bytes();
        let tgt = target.as_bytes();
        for i in 0..n {
            if dp[i] >= INF / 2 {
                continue;
            }
            if src[i] == tgt[i] && dp[i] < dp[i + 1] {
                dp[i + 1] = dp[i];
            }
            for &l in &lens {
                if i + l > n {
                    continue;
                }
                let ss = &source[i..i + l];
                let tt = &target[i..i + l];
                if let (Some(&iu), Some(&iv)) = (ids.get(ss), ids.get(tt)) {
                    if dist[iu][iv] < INF / 2 {
                        let cand = dp[i] + dist[iu][iv];
                        if cand < dp[i + l] {
                            dp[i + l] = cand;
                        }
                    }
                }
            }
        }
        if dp[n] >= INF / 2 {
            -1
        } else {
            dp[n]
        }
    }
}
