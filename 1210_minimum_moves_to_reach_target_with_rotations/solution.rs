// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn minimum_moves(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let start = (0usize, 0usize, 0usize);
        let target = (n - 1, n - 2, 0usize);
        let mut q = VecDeque::new();
        q.push_back((start, 0));
        let mut seen = HashSet::new();
        seen.insert(start);
        while let Some(((r, c, orient), moves)) = q.pop_front() {
            if (r, c, orient) == target {
                return moves;
            }
            let mut nxt = Vec::new();
            if orient == 0 {
                if c + 2 < n && grid[r][c + 2] == 0 {
                    nxt.push((r, c + 1, 0));
                }
                if r + 1 < n && grid[r + 1][c] == 0 && grid[r + 1][c + 1] == 0 {
                    nxt.push((r + 1, c, 0));
                    nxt.push((r, c, 1));
                }
            } else {
                if r + 2 < n && grid[r + 2][c] == 0 {
                    nxt.push((r + 1, c, 1));
                }
                if c + 1 < n && grid[r][c + 1] == 0 && grid[r + 1][c + 1] == 0 {
                    nxt.push((r, c + 1, 1));
                    nxt.push((r, c, 0));
                }
            }
            for st in nxt {
                if seen.insert(st) {
                    q.push_back((st, moves + 1));
                }
            }
        }
        -1
    }
}
