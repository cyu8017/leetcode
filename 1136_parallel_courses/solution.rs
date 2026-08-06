// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

use std::collections::VecDeque;

impl Solution {
    pub fn minimum_semesters(n: i32, relations: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n + 1];
        let mut indeg = vec![0; n + 1];
        for r in relations {
            graph[r[0] as usize].push(r[1] as usize);
            indeg[r[1] as usize] += 1;
        }
        let mut queue = VecDeque::new();
        for i in 1..=n {
            if indeg[i] == 0 {
                queue.push_back(i);
            }
        }
        let mut semesters = 0;
        let mut taken = 0;
        while !queue.is_empty() {
            let size = queue.len();
            semesters += 1;
            for _ in 0..size {
                let u = queue.pop_front().unwrap();
                taken += 1;
                for &v in &graph[u] {
                    indeg[v] -= 1;
                    if indeg[v] == 0 {
                        queue.push_back(v);
                    }
                }
            }
        }
        if taken == n {
            semesters
        } else {
            -1
        }
    }
}
