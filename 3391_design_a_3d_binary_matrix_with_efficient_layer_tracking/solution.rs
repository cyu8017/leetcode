// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

pub struct Matrix3D {
    m: Vec<Vec<Vec<i32>>>,
    ones: Vec<i32>,
    n: usize,
}

impl Matrix3D {
    pub fn new(n: i32) -> Self {
        let n = n as usize;
        Self {
            m: vec![vec![vec![0; n]; n]; n],
            ones: vec![0; n],
            n,
        }
    }

    pub fn set_cell(&mut self, x: i32, y: i32, z: i32) {
        let (x, y, z) = (x as usize, y as usize, z as usize);
        if self.m[x][y][z] == 0 {
            self.m[x][y][z] = 1;
            self.ones[x] += 1;
        }
    }

    pub fn unset_cell(&mut self, x: i32, y: i32, z: i32) {
        let (x, y, z) = (x as usize, y as usize, z as usize);
        if self.m[x][y][z] == 1 {
            self.m[x][y][z] = 0;
            self.ones[x] -= 1;
        }
    }

    pub fn largest_matrix(&self) -> i32 {
        let mut best = -1;
        let mut idx = 0;
        for i in 0..self.n {
            if self.ones[i] >= best {
                best = self.ones[i];
                idx = i;
            }
        }
        idx as i32
    }
}
