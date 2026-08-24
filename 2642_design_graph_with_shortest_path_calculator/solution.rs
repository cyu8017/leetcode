// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub struct Graph {
    g: Vec<Vec<(i32, i32)>>,
}

impl Graph {
    pub fn new(n: i32, edges: Vec<Vec<i32>>) -> Self {
        let mut g = vec![Vec::new(); n as usize];
        for e in edges {
            g[e[0] as usize].push((e[1], e[2]));
        }
        Self { g }
    }

    pub fn add_edge(&mut self, edge: Vec<i32>) {
        self.g[edge[0] as usize].push((edge[1], edge[2]));
    }

    pub fn shortest_path(&self, node1: i32, node2: i32) -> i32 {
        let n = self.g.len();
        let mut dist = vec![1 << 30; n];
        dist[node1 as usize] = 0;
        let mut h = BinaryHeap::new();
        h.push(Reverse((0, node1)));
        while let Some(Reverse((d, u))) = h.pop() {
            if u == node2 {
                return d;
            }
            if d > dist[u as usize] {
                continue;
            }
            for &(to, w) in &self.g[u as usize] {
                let nd = d + w;
                if nd < dist[to as usize] {
                    dist[to as usize] = nd;
                    h.push(Reverse((nd, to)));
                }
            }
        }
        -1
    }
}
