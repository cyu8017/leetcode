// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Eq, PartialEq, Clone, Copy)]
struct State {
    dist: i32,
    row: usize,
    col: usize,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.dist.cmp(&self.dist)
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn shortest_distance(maze: Vec<Vec<i32>>, start: Vec<i32>, destination: Vec<i32>) -> i32 {
        let rows = maze.len();
        let cols = maze[0].len();
        let target_row = destination[0] as usize;
        let target_col = destination[1] as usize;
        let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];

        let mut best = vec![vec![i32::MAX; cols]; rows];
        let mut heap = BinaryHeap::new();
        heap.push(State {
            dist: 0,
            row: start[0] as usize,
            col: start[1] as usize,
        });

        while let Some(current) = heap.pop() {
            if current.row == target_row && current.col == target_col {
                return current.dist;
            }
            if best[current.row][current.col] <= current.dist {
                continue;
            }
            best[current.row][current.col] = current.dist;

            for (dr, dc) in directions {
                let mut next_row = current.row as i32;
                let mut next_col = current.col as i32;
                let mut traveled = 0;
                loop {
                    let candidate_row = next_row + dr;
                    let candidate_col = next_col + dc;
                    if candidate_row < 0
                        || candidate_col < 0
                        || candidate_row as usize >= rows
                        || candidate_col as usize >= cols
                        || maze[candidate_row as usize][candidate_col as usize] == 1
                    {
                        break;
                    }
                    next_row = candidate_row;
                    next_col = candidate_col;
                    traveled += 1;
                }
                if next_row as usize == current.row && next_col as usize == current.col {
                    continue;
                }
                let new_dist = current.dist + traveled;
                let next_row = next_row as usize;
                let next_col = next_col as usize;
                if new_dist < best[next_row][next_col] {
                    heap.push(State {
                        dist: new_dist,
                        row: next_row,
                        col: next_col,
                    });
                }
            }
        }
        -1
    }
}
