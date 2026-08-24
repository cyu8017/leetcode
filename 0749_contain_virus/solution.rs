// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

use std::collections::HashSet;

impl Solution {
    pub fn contain_virus(mut is_infected: Vec<Vec<i32>>) -> i32 {
        let m = is_infected.len();
        let n = is_infected[0].len();
        let mut walls = 0;
        loop {
            let mut seen = HashSet::new();
            let mut regions = Vec::new();
            let mut frontiers = Vec::new();
            let mut perimeters = Vec::new();

            for i in 0..m {
                for j in 0..n {
                    if is_infected[i][j] == 1 && seen.insert((i, j)) {
                        let mut stack = vec![(i, j)];
                        let mut region = HashSet::new();
                        let mut frontier = HashSet::new();
                        let mut perimeter = 0;
                        while let Some((r, c)) = stack.pop() {
                            region.insert((r, c));
                            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                                let nr = r as i32 + dr;
                                let nc = c as i32 + dc;
                                if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                                    continue;
                                }
                                let (nr, nc) = (nr as usize, nc as usize);
                                if is_infected[nr][nc] == 1 && seen.insert((nr, nc)) {
                                    stack.push((nr, nc));
                                } else if is_infected[nr][nc] == 0 {
                                    frontier.insert((nr, nc));
                                    perimeter += 1;
                                }
                            }
                        }
                        regions.push(region);
                        frontiers.push(frontier);
                        perimeters.push(perimeter);
                    }
                }
            }

            if regions.is_empty() {
                break;
            }
            let mut quarantine = 0;
            for i in 1..regions.len() {
                if frontiers[i].len() > frontiers[quarantine].len() {
                    quarantine = i;
                }
            }
            if frontiers[quarantine].is_empty() {
                break;
            }
            walls += perimeters[quarantine];
            for &(r, c) in &regions[quarantine] {
                is_infected[r][c] = -1;
            }
            for (index, frontier) in frontiers.iter().enumerate() {
                if index == quarantine {
                    continue;
                }
                for &(r, c) in frontier {
                    is_infected[r][c] = 1;
                }
            }
        }
        walls
    }
}
