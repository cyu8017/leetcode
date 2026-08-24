// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

use std::collections::VecDeque;

impl Solution {
    pub fn minimum_time(n: i32, relations: Vec<Vec<i32>>, time: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n + 1];
        let mut indeg = vec![0; n + 1];
        let mut dist = vec![0; n + 1];
        for e in relations {
            g[e[0] as usize].push(e[1] as usize);
            indeg[e[1] as usize] += 1;
        }
        let mut q = VecDeque::new();
        for i in 1..=n {
            dist[i] = time[i - 1];
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }
        while let Some(u) = q.pop_front() {
            for &v in &g[u] {
                dist[v] = dist[v].max(dist[u] + time[v - 1]);
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    q.push_back(v);
                }
            }
        }
        *dist[1..].iter().max().unwrap()
    }
}
