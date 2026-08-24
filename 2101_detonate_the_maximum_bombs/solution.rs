// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

use std::collections::VecDeque;

impl Solution {
    pub fn maximum_detonation(bombs: Vec<Vec<i32>>) -> i32 {
        let n = bombs.len();
        let mut g = vec![Vec::new(); n];
        for i in 0..n {
            let (x1, y1, r1) = (bombs[i][0] as i64, bombs[i][1] as i64, bombs[i][2] as i64);
            for j in 0..n {
                if i == j {
                    continue;
                }
                let dx = bombs[j][0] as i64 - x1;
                let dy = bombs[j][1] as i64 - y1;
                if dx * dx + dy * dy <= r1 * r1 {
                    g[i].push(j);
                }
            }
        }
        let mut ans = 0;
        for i in 0..n {
            let mut vis = vec![false; n];
            let mut q = VecDeque::new();
            q.push_back(i);
            vis[i] = true;
            let mut cnt = 0;
            while let Some(u) = q.pop_front() {
                cnt += 1;
                for &v in &g[u] {
                    if !vis[v] {
                        vis[v] = true;
                        q.push_back(v);
                    }
                }
            }
            ans = ans.max(cnt);
        }
        ans
    }
}
