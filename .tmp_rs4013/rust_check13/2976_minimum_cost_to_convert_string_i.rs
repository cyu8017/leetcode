#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

impl Solution {
    pub fn minimum_cost(
        source: String,
        target: String,
        original: Vec<char>,
        changed: Vec<char>,
        cost: Vec<i32>,
    ) -> i64 {
        const INF: i64 = 1i64 << 60;
        let mut dist = vec![vec![INF; 26]; 26];
        for i in 0..26 {
            dist[i][i] = 0;
        }
        for i in 0..original.len() {
            let u = (original[i] as u8 - b'a') as usize;
            let v = (changed[i] as u8 - b'a') as usize;
            let ww = cost[i] as i64;
            if ww < dist[u][v] {
                dist[u][v] = ww;
            }
        }
        for k in 0..26 {
            for i in 0..26 {
                for j in 0..26 {
                    if dist[i][k] + dist[k][j] < dist[i][j] {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        let src = source.as_bytes();
        let tgt = target.as_bytes();
        let mut ans = 0i64;
        for i in 0..src.len() {
            let a = (src[i] - b'a') as usize;
            let b = (tgt[i] - b'a') as usize;
            if dist[a][b] >= INF / 2 {
                return -1;
            }
            ans += dist[a][b];
        }
        ans
    }
}
