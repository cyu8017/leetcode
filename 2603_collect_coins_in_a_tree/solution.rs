// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn collect_the_coins(coins: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = coins.len();
        let mut g: Vec<HashSet<i32>> = vec![HashSet::new(); n];
        for e in edges {
            g[e[0] as usize].insert(e[1]);
            g[e[1] as usize].insert(e[0]);
        }
        let mut deg: Vec<i32> = g.iter().map(|s| s.len() as i32).collect();
        let mut q = VecDeque::new();
        for i in 0..n {
            if deg[i] == 1 && coins[i] == 0 {
                q.push_back(i);
            }
        }
        while let Some(u) = q.pop_front() {
            let neigh: Vec<i32> = g[u].iter().copied().collect();
            for v in neigh {
                g[v as usize].remove(&(u as i32));
                deg[v as usize] -= 1;
                if deg[v as usize] == 1 && coins[v as usize] == 0 {
                    q.push_back(v as usize);
                }
            }
            g[u].clear();
            deg[u] = 0;
        }
        for _ in 0..2 {
            let leaves: Vec<usize> = (0..n).filter(|&i| deg[i] == 1).collect();
            for u in leaves {
                let neigh: Vec<i32> = g[u].iter().copied().collect();
                for v in neigh {
                    g[v as usize].remove(&(u as i32));
                    deg[v as usize] -= 1;
                }
                g[u].clear();
                deg[u] = 0;
            }
        }
        let mut remain = 0;
        for s in g {
            remain += s.len() as i32;
        }
        remain
    }
}
