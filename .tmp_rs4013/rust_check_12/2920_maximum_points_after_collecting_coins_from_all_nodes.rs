struct Solution;
// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_points(edges: Vec<Vec<i32>>, coins: Vec<i32>, k: i32) -> i32 {
        let n = coins.len();
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        fn dfs(
            u: usize,
            p: i32,
            mut shifts: i32,
            g: &[Vec<usize>],
            coins: &[i32],
            k: i32,
            memo: &mut HashMap<(usize, i32), i32>,
        ) -> i32 {
            if shifts > 14 {
                shifts = 14;
            }
            if let Some(&v) = memo.get(&(u, shifts)) {
                return v;
            }
            let c = coins[u] >> shifts;
            let mut opt1 = c - k;
            let mut opt2 = c / 2;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                opt1 += dfs(v, u as i32, shifts, g, coins, k, memo);
                opt2 += dfs(v, u as i32, shifts + 1, g, coins, k, memo);
            }
            let best = opt1.max(opt2);
            memo.insert((u, shifts), best);
            best
        }
        let mut memo = HashMap::new();
        dfs(0, -1, 0, &g, &coins, k, &mut memo)
    }
}

fn main() {}
