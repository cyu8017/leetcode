// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

use std::collections::HashSet;

impl Solution {
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        fn encode(x: i32, y: i32) -> i64 {
            ((x as i64 + 30000) << 20) | (y as i64 + 30000)
        }
        let blocked: HashSet<i64> = obstacles
            .iter()
            .map(|o| encode(o[0], o[1]))
            .collect();
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut x = 0;
        let mut y = 0;
        let mut d = 0;
        let mut best = 0;
        for cmd in commands {
            if cmd == -1 {
                d = (d + 1) % 4;
            } else if cmd == -2 {
                d = (d + 3) % 4;
            } else {
                let (dx, dy) = dirs[d];
                for _ in 0..cmd {
                    let nx = x + dx;
                    let ny = y + dy;
                    if blocked.contains(&encode(nx, ny)) {
                        break;
                    }
                    x = nx;
                    y = ny;
                }
                best = best.max(x * x + y * y);
            }
        }
        best
    }
}
