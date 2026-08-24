// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn minimum_cost(target: String, words: Vec<String>, costs: Vec<i32>) -> i32 {
        const BASE: i64 = 13331;
        const MOD: i64 = 998244353;
        const INF: i32 = i32::MAX / 2;
        let n = target.len();
        let tb = target.as_bytes();
        let mut p = vec![0i64; n + 1];
        let mut h = vec![0i64; n + 1];
        p[0] = 1;
        for i in 1..=n {
            p[i] = p[i - 1] * BASE % MOD;
            h[i] = (h[i - 1] * BASE + tb[i - 1] as i64) % MOD;
        }
        let query = |l: usize, r: usize| -> i64 {
            (h[r] - h[l - 1] * p[r - l + 1] % MOD + MOD) % MOD
        };
        let mut f = vec![INF; n + 1];
        f[0] = 0;
        let mut ss: HashSet<usize> = HashSet::new();
        for w in &words {
            ss.insert(w.len());
        }
        let mut lengths: Vec<usize> = ss.into_iter().collect();
        lengths.sort_unstable();
        let mut d: HashMap<i64, i32> = HashMap::new();
        for (i, w) in words.iter().enumerate() {
            let mut x = 0i64;
            for &c in w.as_bytes() {
                x = (x * BASE + c as i64) % MOD;
            }
            let e = d.entry(x).or_insert(INF);
            if costs[i] < *e {
                *e = costs[i];
            }
        }
        for i in 1..=n {
            for &j in &lengths {
                if j > i {
                    break;
                }
                let x = query(i - j + 1, i);
                if let Some(&c) = d.get(&x) {
                    f[i] = f[i].min(f[i - j] + c);
                }
            }
        }
        if f[n] >= INF { -1 } else { f[n] }
    }
}
