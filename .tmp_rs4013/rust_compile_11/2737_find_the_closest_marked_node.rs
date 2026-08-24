struct Solution;
fn main() {}

// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};

impl Solution {
    pub fn minimum_distance(n: i32, edges: Vec<Vec<i32>>, s: i32, marked: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::<(usize, i32)>::new(); n];
        for e in edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
        }
        let mark: HashSet<i32> = marked.into_iter().collect();
        let mut dist = vec![i32::MAX / 4; n];
        dist[s as usize] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0, s as usize)));
        while let Some(Reverse((d, u))) = pq.pop() {
            if mark.contains(&(u as i32)) {
                return d;
            }
            if d > dist[u] {
                continue;
            }
            for &(v, w) in &g[u] {
                if d + w < dist[v] {
                    dist[v] = d + w;
                    pq.push(Reverse((dist[v], v)));
                }
            }
        }
        -1
    }
}
