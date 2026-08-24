// LeetCode 4003 - Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_cost(m: i32, n: i32, penalty: Vec<Vec<i32>>) -> i64 {
        const INF: i64 = 1 << 60;
        let m = m as usize;
        let n = n as usize;
        let mut dist = vec![vec![[INF; 2]; n]; m];
        dist[0][0][1] = 1;
        let mut pq: BinaryHeap<Reverse<(i64, usize, usize, usize)>> = BinaryHeap::new();
        pq.push(Reverse((1, 0, 0, 1)));
        let dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)];
        while let Some(Reverse((d, i, j, k))) = pq.pop() {
            if i == m - 1 && j == n - 1 {
                return d;
            }
            if d > dist[i][j][k] {
                continue;
            }
            let p = penalty[i][j];
            let nd = d + p as i64;
            if nd < dist[i][j][k ^ 1] {
                dist[i][j][k ^ 1] = nd;
                pq.push(Reverse((nd, i, j, k ^ 1)));
            }
            for (idx, &(di, dj)) in dirs.iter().enumerate() {
                let x = i as i32 + di;
                let y = j as i32 + dj;
                if x >= 0 && (x as usize) < m && y >= 0 && (y as usize) < n {
                    let nd = d + ((x + 1) as i64 * (y + 1) as i64 + (((idx & 1) as i32 ^ k as i32) * p) as i64);
                    let xu = x as usize;
                    let yu = y as usize;
                    if nd < dist[xu][yu][k ^ 1] {
                        dist[xu][yu][k ^ 1] = nd;
                        pq.push(Reverse((nd, xu, yu, k ^ 1)));
                    }
                }
            }
        }
        -1
    }
}
