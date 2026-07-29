// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn is_escape_possible(blocked: Vec<Vec<i32>>, source: Vec<i32>, target: Vec<i32>) -> bool {
        let blocked_set: HashSet<(i32, i32)> =
            blocked.iter().map(|b| (b[0], b[1])).collect();
        let b = blocked.len();
        let limit = b * b.saturating_sub(1) / 2;

        fn bfs(
            start: &[i32],
            goal: &[i32],
            blocked_set: &HashSet<(i32, i32)>,
            limit: usize,
        ) -> bool {
            let mut queue = VecDeque::new();
            let mut seen = HashSet::new();
            queue.push_back((start[0], start[1]));
            seen.insert((start[0], start[1]));
            while let Some((r, c)) = queue.pop_front() {
                if seen.len() > limit {
                    return true;
                }
                if r == goal[0] && c == goal[1] {
                    return true;
                }
                for (nr, nc) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] {
                    if (0..1_000_000).contains(&nr)
                        && (0..1_000_000).contains(&nc)
                        && !blocked_set.contains(&(nr, nc))
                        && seen.insert((nr, nc))
                    {
                        queue.push_back((nr, nc));
                    }
                }
            }
            false
        }

        bfs(&source, &target, &blocked_set, limit) && bfs(&target, &source, &blocked_set, limit)
    }
}
