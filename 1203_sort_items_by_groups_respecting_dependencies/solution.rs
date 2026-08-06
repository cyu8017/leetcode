// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn sort_items(
        n: i32,
        mut m: i32,
        mut group: Vec<i32>,
        before_items: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        let n = n as usize;
        for i in 0..n {
            if group[i] == -1 {
                group[i] = m;
                m += 1;
            }
        }
        let m = m as usize;
        let mut item_graph = vec![Vec::new(); n];
        let mut item_indeg = vec![0; n];
        let mut group_graph = vec![HashSet::new(); m];
        let mut group_indeg = vec![0; m];
        for v in 0..n {
            for &u in &before_items[v] {
                let u = u as usize;
                item_graph[u].push(v);
                item_indeg[v] += 1;
                let gu = group[u] as usize;
                let gv = group[v] as usize;
                if gu != gv && group_graph[gu].insert(gv) {
                    group_indeg[gv] += 1;
                }
            }
        }
        fn topo(graph: &[Vec<usize>], mut indeg: Vec<i32>) -> Option<Vec<usize>> {
            let mut q = VecDeque::new();
            for (i, &d) in indeg.iter().enumerate() {
                if d == 0 {
                    q.push_back(i);
                }
            }
            let mut order = Vec::new();
            while let Some(u) = q.pop_front() {
                order.push(u);
                for &v in &graph[u] {
                    indeg[v] -= 1;
                    if indeg[v] == 0 {
                        q.push_back(v);
                    }
                }
            }
            if order.len() == graph.len() {
                Some(order)
            } else {
                None
            }
        }
        let g_adj: Vec<Vec<usize>> = group_graph
            .into_iter()
            .map(|s| s.into_iter().collect())
            .collect();
        let items = match topo(&item_graph, item_indeg) {
            Some(v) => v,
            None => return vec![],
        };
        let groups = match topo(&g_adj, group_indeg) {
            Some(v) => v,
            None => return vec![],
        };
        let mut buckets = vec![Vec::new(); m];
        for item in items {
            buckets[group[item] as usize].push(item as i32);
        }
        let mut ans = Vec::new();
        for g in groups {
            ans.extend(buckets[g].iter().copied());
        }
        ans
    }
}
