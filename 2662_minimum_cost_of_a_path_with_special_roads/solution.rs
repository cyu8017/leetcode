// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_cost(start: Vec<i32>, target: Vec<i32>, special_roads: Vec<Vec<i32>>) -> i32 {
        let mut points = vec![start.clone(), target.clone()];
        for r in &special_roads {
            points.push(vec![r[0], r[1]]);
            points.push(vec![r[2], r[3]]);
        }
        let n = points.len();
        let dist_man = |a: &[i32], b: &[i32]| (a[0] - b[0]).abs() + (a[1] - b[1]).abs();
        let mut g = vec![Vec::new(); n];
        for i in 0..n {
            for j in 0..n {
                if i != j {
                    g[i].push((j, dist_man(&points[i], &points[j])));
                }
            }
        }
        for r in &special_roads {
            let mut u = -1;
            let mut v = -1;
            for i in 0..n {
                if points[i][0] == r[0] && points[i][1] == r[1] {
                    u = i as i32;
                }
                if points[i][0] == r[2] && points[i][1] == r[3] {
                    v = i as i32;
                }
            }
            if u >= 0 && v >= 0 {
                g[u as usize].push((v as usize, r[4]));
            }
        }
        let mut dist = vec![i32::MAX / 4; n];
        dist[0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0, 0usize)));
        while let Some(Reverse((cost, id))) = pq.pop() {
            if cost > dist[id] {
                continue;
            }
            for &(to, w) in &g[id] {
                if cost + w < dist[to] {
                    dist[to] = cost + w;
                    pq.push(Reverse((dist[to], to)));
                }
            }
        }
        dist[1]
    }
}
