// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn min_push_box(grid: Vec<Vec<char>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut box_pos = (0, 0);
        let mut player = (0, 0);
        let mut target = (0, 0);
        for r in 0..m {
            for c in 0..n {
                match grid[r][c] {
                    'B' => box_pos = (r, c),
                    'S' => player = (r, c),
                    'T' => target = (r, c),
                    _ => {}
                }
            }
        }
        let reachable = |start: (usize, usize), blocked: (usize, usize)| -> HashSet<(usize, usize)> {
            let mut seen = HashSet::new();
            seen.insert(start);
            let mut stack = vec![start];
            while let Some(cur) = stack.pop() {
                for (dr, dc) in [(1isize, 0), (-1, 0), (0, 1), (0, -1)] {
                    let nr = cur.0 as isize + dr;
                    let nc = cur.1 as isize + dc;
                    if nr >= 0 && nr < m as isize && nc >= 0 && nc < n as isize {
                        let nxt = (nr as usize, nc as usize);
                        if grid[nxt.0][nxt.1] != '#' && nxt != blocked && seen.insert(nxt) {
                            stack.push(nxt);
                        }
                    }
                }
            }
            seen
        };
        let mut q = VecDeque::new();
        q.push_back((box_pos, player, 0));
        let mut seen = HashSet::new();
        seen.insert((box_pos, player));
        while let Some((b, p, push)) = q.pop_front() {
            if b == target {
                return push;
            }
            let can = reachable(p, b);
            for (dr, dc) in [(1isize, 0), (-1, 0), (0, 1), (0, -1)] {
                let stand = (b.0 as isize - dr, b.1 as isize - dc);
                let nb = (b.0 as isize + dr, b.1 as isize + dc);
                if stand.0 >= 0
                    && stand.1 >= 0
                    && nb.0 >= 0
                    && nb.1 >= 0
                    && stand.0 < m as isize
                    && stand.1 < n as isize
                    && nb.0 < m as isize
                    && nb.1 < n as isize
                {
                    let stand = (stand.0 as usize, stand.1 as usize);
                    let nb = (nb.0 as usize, nb.1 as usize);
                    if can.contains(&stand) && grid[nb.0][nb.1] != '#' {
                        let st = (nb, b);
                        if seen.insert(st) {
                            q.push_back((nb, b, push + 1));
                        }
                    }
                }
            }
        }
        -1
    }
}
