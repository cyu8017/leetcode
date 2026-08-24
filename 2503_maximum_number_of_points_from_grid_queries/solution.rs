// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn max_points(grid: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        let m = grid.len();
        let n = grid[0].len();
        let mut order: Vec<usize> = (0..queries.len()).collect();
        order.sort_by_key(|&i| queries[i]);
        let mut ans = vec![0; queries.len()];
        let mut visited = vec![vec![false; n]; m];
        let mut pq: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
        pq.push(Reverse((grid[0][0], 0, 0)));
        visited[0][0] = true;
        let mut points = 0;
        let dirs = [(1isize, 0isize), (-1, 0), (0, 1), (0, -1)];
        for qi in order {
            let q = queries[qi];
            loop {
                let should_pop = match pq.peek() {
                    Some(Reverse((v, _, _))) => *v < q,
                    None => false,
                };
                if !should_pop {
                    break;
                }
                let Reverse((_, r, c)) = pq.pop().unwrap();
                points += 1;
                for (dr, dc) in dirs {
                    let nr = r as isize + dr;
                    let nc = c as isize + dc;
                    if nr >= 0 && nr < m as isize && nc >= 0 && nc < n as isize {
                        let (nr, nc) = (nr as usize, nc as usize);
                        if !visited[nr][nc] {
                            visited[nr][nc] = true;
                            pq.push(Reverse((grid[nr][nc], nr, nc)));
                        }
                    }
                }
            }
            ans[qi] = points;
        }
        ans
    }
}
