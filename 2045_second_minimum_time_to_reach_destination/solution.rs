// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

use std::collections::VecDeque;

impl Solution {
    pub fn second_minimum(n: i32, edges: Vec<Vec<i32>>, time: i32, change: i32) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n + 1];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut dist1 = vec![-1; n + 1];
        let mut dist2 = vec![-1; n + 1];
        let mut q = VecDeque::new();
        q.push_back((1, 0));
        dist1[1] = 0;
        while let Some((u, d)) = q.pop_front() {
            for &v in &g[u] {
                let nd = d + 1;
                if dist1[v] == -1 {
                    dist1[v] = nd;
                    q.push_back((v, nd));
                } else if dist2[v] == -1 && nd > dist1[v] {
                    dist2[v] = nd;
                    q.push_back((v, nd));
                }
            }
        }
        let steps = dist2[n];
        let mut ans = 0;
        for _ in 0..steps {
            if (ans / change) % 2 == 1 {
                ans += change - ans % change;
            }
            ans += time;
        }
        ans
    }
}
