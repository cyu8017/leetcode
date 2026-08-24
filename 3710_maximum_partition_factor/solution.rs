// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

use std::collections::VecDeque;

impl Solution {
    pub fn max_partition_factor(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        if n == 2 {
            return 0;
        }
        let dist = |i: usize, j: usize| -> i32 {
            (points[i][0] - points[j][0]).abs() + (points[i][1] - points[j][1]).abs()
        };
        let ok = |d: i32| -> bool {
            let mut g = vec![Vec::new(); n];
            for i in 0..n {
                for j in i + 1..n {
                    if dist(i, j) < d {
                        g[i].push(j);
                        g[j].push(i);
                    }
                }
            }
            let mut color = vec![-1i32; n];
            for i in 0..n {
                if color[i] != -1 {
                    continue;
                }
                let mut q = VecDeque::new();
                q.push_back(i);
                color[i] = 0;
                while let Some(u) = q.pop_front() {
                    for &v in &g[u] {
                        if color[v] == -1 {
                            color[v] = color[u] ^ 1;
                            q.push_back(v);
                        } else if color[v] == color[u] {
                            return false;
                        }
                    }
                }
            }
            true
        };
        let mut lo = 0;
        let mut hi = 0;
        for i in 0..n {
            for j in i + 1..n {
                hi = hi.max(dist(i, j));
            }
        }
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if ok(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}
