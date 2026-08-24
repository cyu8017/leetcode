// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

use std::cmp::Reverse;
use std::collections::{BinaryHeap, VecDeque};

impl Solution {
    pub fn find_answer(n: i32, edges: Vec<Vec<i32>>) -> Vec<bool> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for (i, e) in edges.iter().enumerate() {
            let (a, b, w) = (e[0] as usize, e[1] as usize, e[2]);
            g[a].push((b, w, i));
            g[b].push((a, w, i));
        }
        const INF: i32 = 1 << 30;
        let mut dist = vec![INF; n];
        dist[0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0i32, 0usize)));
        while let Some(Reverse((da, a))) = pq.pop() {
            if da > dist[a] {
                continue;
            }
            for &(b, w, _) in &g[a] {
                if dist[b] > dist[a] + w {
                    dist[b] = dist[a] + w;
                    pq.push(Reverse((dist[b], b)));
                }
            }
        }
        let mut ans = vec![false; edges.len()];
        if dist[n - 1] == INF {
            return ans;
        }
        let mut q = VecDeque::new();
        q.push_back(n - 1);
        while let Some(a) = q.pop_front() {
            for &(b, w, i) in &g[a] {
                if dist[a] == dist[b] + w {
                    ans[i] = true;
                    q.push_back(b);
                }
            }
        }
        ans
    }
}
