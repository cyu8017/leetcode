struct Solution;
// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn shortest_path(n: i32, edges: Vec<Vec<i32>>, labels: String, k: i32) -> i64 {
        let n = n as usize;
        let k = k as usize;
        let mut graph = vec![Vec::new(); n];
        for edge in &edges {
            graph[edge[0] as usize].push((edge[1] as usize, edge[2]));
        }
        let labels = labels.into_bytes();
        const INFINITY: i64 = ((u64::MAX) >> 2) as i64;
        let mut distances = vec![vec![INFINITY; k + 1]; n];
        distances[0][1] = 0;
        let mut queue: BinaryHeap<Reverse<(i64, usize, usize)>> = BinaryHeap::new();
        queue.push(Reverse((0, 0, 1)));
        while let Some(Reverse((distance, node, run))) = queue.pop() {
            if distance != distances[node][run] {
                continue;
            }
            if node == n - 1 {
                return distance;
            }
            for &(to, weight) in &graph[node] {
                let next_run = if labels[node] == labels[to] { run + 1 } else { 1 };
                if next_run > k {
                    continue;
                }
                let next_distance = distance + weight as i64;
                if next_distance < distances[to][next_run] {
                    distances[to][next_run] = next_distance;
                    queue.push(Reverse((next_distance, to, next_run)));
                }
            }
        }
        -1
    }
}

fn main() {}
