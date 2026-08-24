// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

use std::collections::HashMap;

pub struct NeighborSum {
    grid: Vec<Vec<i32>>,
    d: HashMap<i32, (i32, i32)>,
}

impl NeighborSum {
    pub fn new(grid: Vec<Vec<i32>>) -> Self {
        let mut d = HashMap::new();
        for i in 0..grid.len() {
            for j in 0..grid[i].len() {
                d.insert(grid[i][j], (i as i32, j as i32));
            }
        }
        Self { grid, d }
    }

    fn cal(&self, value: i32, k: usize) -> i32 {
        let dirs = [[-1, 0, 1, 0, -1], [-1, 1, 1, -1, -1]];
        let p = self.d[&value];
        let mut s = 0;
        for q in 0..4 {
            let x = p.0 + dirs[k][q];
            let y = p.1 + dirs[k][q + 1];
            if x >= 0 && x < self.grid.len() as i32 && y >= 0 && y < self.grid[0].len() as i32 {
                s += self.grid[x as usize][y as usize];
            }
        }
        s
    }

    pub fn adjacent_sum(&self, value: i32) -> i32 {
        self.cal(value, 0)
    }

    pub fn diagonal_sum(&self, value: i32) -> i32 {
        self.cal(value, 1)
    }
}
