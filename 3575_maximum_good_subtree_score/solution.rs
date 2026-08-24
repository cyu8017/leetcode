// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

use std::collections::HashMap;

impl Solution {
    pub fn good_subtree_sum(vals: Vec<i32>, par: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = vals.len();
        let mut g = vec![Vec::<usize>::new(); n];
        for i in 1..n {
            g[par[i] as usize].push(i);
        }
        fn digit_mask(mut x: i32) -> (i32, bool, i32) {
            let v = x;
            let mut mask = 0;
            if x == 0 {
                return (1, true, 0);
            }
            while x > 0 {
                let d = x % 10;
                if mask & (1 << d) != 0 {
                    return (0, false, 0);
                }
                mask |= 1 << d;
                x /= 10;
            }
            (mask, true, v)
        }
        fn dfs(u: usize, g: &[Vec<usize>], vals: &[i32], ans: &mut i32) -> HashMap<i32, i32> {
            let mut dp = HashMap::new();
            dp.insert(0, 0);
            let (mask, ok, v) = digit_mask(vals[u]);
            if ok {
                dp.insert(mask, v);
            }
            for &c in &g[u] {
                let child = dfs(c, g, vals, ans);
                let mut ndp: HashMap<i32, i32> = HashMap::new();
                for (&m1, &s1) in &dp {
                    for (&m2, &s2) in &child {
                        if (m1 & m2) == 0 {
                            let nm = m1 | m2;
                            ndp.insert(nm, ndp.get(&nm).copied().unwrap_or(0).max(s1 + s2));
                        }
                    }
                }
                for (&m, &s) in &dp {
                    ndp.insert(m, ndp.get(&m).copied().unwrap_or(0).max(s));
                }
                for (&m, &s) in &child {
                    ndp.insert(m, ndp.get(&m).copied().unwrap_or(0).max(s));
                }
                dp = ndp;
            }
            let best = dp.values().copied().max().unwrap_or(0);
            *ans = (*ans + best) % MOD;
            dp
        }
        let mut ans = 0;
        dfs(0, &g, &vals, &mut ans);
        ans
    }
}
