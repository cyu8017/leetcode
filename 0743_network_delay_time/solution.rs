// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n + 1];
        for edge in times {
            graph[edge[0] as usize].push((edge[1] as usize, edge[2]));
        }
        const INF: i32 = i32::MAX / 4;
        let mut dist = vec![INF; n + 1];
        dist[k as usize] = 0;
        let mut heap = BinaryHeap::new();
        heap.push(Reverse((0, k as usize)));
        while let Some(Reverse((d, node))) = heap.pop() {
            if d > dist[node] {
                continue;
            }
            for &(nei, weight) in &graph[node] {
                let nd = d + weight;
                if nd < dist[nei] {
                    dist[nei] = nd;
                    heap.push(Reverse((nd, nei)));
                }
            }
        }
        let ans = *dist[1..].iter().max().unwrap();
        if ans == INF {
            -1
        } else {
            ans
        }
    }
}
