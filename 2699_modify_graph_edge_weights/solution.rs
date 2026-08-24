// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn modified_graph_edges(
        n: i32,
        mut edges: Vec<Vec<i32>>,
        source: i32,
        destination: i32,
        target: i32,
    ) -> Vec<Vec<i32>> {
        const INF: i32 = 2_000_000_000;
        let n = n as usize;
        let dijkstra = |edges: &[Vec<i32>], ignore_neg: bool| -> Vec<i32> {
            let mut dist = vec![INF; n];
            dist[source as usize] = 0;
            let mut pq = BinaryHeap::new();
            pq.push(Reverse((0, source)));
            while let Some(Reverse((d, u))) = pq.pop() {
                if d != dist[u as usize] {
                    continue;
                }
                for e in edges {
                    let a = e[0];
                    let b = e[1];
                    let mut w = e[2];
                    if a != u && b != u {
                        continue;
                    }
                    let to = if a == u { b } else { a };
                    if w == -1 {
                        if ignore_neg {
                            continue;
                        }
                        w = 1;
                    }
                    if d + w < dist[to as usize] {
                        dist[to as usize] = d + w;
                        pq.push(Reverse((dist[to as usize], to)));
                    }
                }
            }
            dist
        };
        let mut d = dijkstra(&edges, true);
        if d[destination as usize] < target {
            return vec![];
        }
        let mut matched = d[destination as usize] == target;
        for i in 0..edges.len() {
            if edges[i][2] != -1 {
                continue;
            }
            if matched {
                edges[i][2] = INF;
                continue;
            }
            edges[i][2] = 1;
            d = dijkstra(&edges, false);
            if d[destination as usize] <= target {
                edges[i][2] += target - d[destination as usize];
                matched = true;
            }
        }
        d = dijkstra(&edges, false);
        if d[destination as usize] != target {
            return vec![];
        }
        edges
    }
}
