// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Eq, PartialEq, Clone)]
struct State {
    dist: i32,
    path: String,
    row: usize,
    col: usize,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        match self.dist.cmp(&other.dist) {
            Ordering::Equal => other.path.cmp(&self.path),
            ordering => ordering.reverse(),
        }
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn find_shortest_way(maze: Vec<Vec<i32>>, ball: Vec<i32>, hole: Vec<i32>) -> String {
        let rows = maze.len();
        let cols = maze[0].len();
        let hole_row = hole[0] as usize;
        let hole_col = hole[1] as usize;
        let directions = [(1, 0), (0, -1), (0, 1), (-1, 0)];
        let labels = ['d', 'l', 'r', 'u'];

        let roll = |row: usize, col: usize, dr: i32, dc: i32| {
            let mut row = row as i32;
            let mut col = col as i32;
            let mut distance = 0;
            loop {
                let next_row = row + dr;
                let next_col = col + dc;
                if next_row < 0
                    || next_col < 0
                    || next_row as usize >= rows
                    || next_col as usize >= cols
                    || maze[next_row as usize][next_col as usize] == 1
                {
                    break;
                }
                row = next_row;
                col = next_col;
                distance += 1;
                if row as usize == hole_row && col as usize == hole_col {
                    break;
                }
            }
            (row as usize, col as usize, distance)
        };

        let mut best = vec![(i32::MAX, String::new()); rows * cols];
        let mut heap = BinaryHeap::new();
        heap.push(State {
            dist: 0,
            path: String::new(),
            row: ball[0] as usize,
            col: ball[1] as usize,
        });

        while let Some(current) = heap.pop() {
            let state_index = current.row * cols + current.col;
            if best[state_index].0 < current.dist
                || (best[state_index].0 == current.dist && best[state_index].1 <= current.path)
            {
                continue;
            }
            best[state_index] = (current.dist, current.path.clone());
            if current.row == hole_row && current.col == hole_col {
                return current.path;
            }

            for index in 0..4 {
                let (dr, dc) = directions[index];
                let (next_row, next_col, traveled) = roll(current.row, current.col, dr, dc);
                if next_row == current.row && next_col == current.col {
                    continue;
                }
                let new_dist = current.dist + traveled;
                let mut new_path = current.path.clone();
                new_path.push(labels[index]);
                let target_index = next_row * cols + next_col;
                if new_dist < best[target_index].0
                    || (new_dist == best[target_index].0 && new_path < best[target_index].1)
                {
                    heap.push(State {
                        dist: new_dist,
                        path: new_path,
                        row: next_row,
                        col: next_col,
                    });
                }
            }
        }
        "impossible".to_string()
    }
}
