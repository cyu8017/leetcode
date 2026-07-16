// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

pub struct NumMatrix {
    matrix: Vec<Vec<i32>>,
    tree: Vec<Vec<i32>>,
    rows: i32,
    cols: i32,
}

impl NumMatrix {
    pub fn new(matrix: Vec<Vec<i32>>) -> Self {
        let rows = matrix.len() as i32;
        let cols = if rows > 0 { matrix[0].len() as i32 } else { 0 };
        let mut obj = Self {
            matrix,
            tree: vec![vec![0; cols as usize + 1]; rows as usize + 1],
            rows,
            cols,
        };
        for row in 0..rows {
            for col in 0..cols {
                let value = obj.matrix[row as usize][col as usize];
                obj.add(row + 1, col + 1, value);
            }
        }
        obj
    }

    fn add(&mut self, mut row: i32, col: i32, delta: i32) {
        let start_col = col;
        while row <= self.rows {
            let mut col_index = start_col;
            while col_index <= self.cols {
                self.tree[row as usize][col_index as usize] += delta;
                col_index += col_index & -col_index;
            }
            row += row & -row;
        }
    }

    fn prefix(&self, mut row: i32, mut col: i32) -> i32 {
        let mut total = 0;
        while row > 0 {
            let mut col_index = col;
            while col_index > 0 {
                total += self.tree[row as usize][col_index as usize];
                col_index -= col_index & -col_index;
            }
            row -= row & -row;
        }
        total
    }

    pub fn update(&mut self, row: i32, col: i32, val: i32) {
        let delta = val - self.matrix[row as usize][col as usize];
        self.matrix[row as usize][col as usize] = val;
        self.add(row + 1, col + 1, delta);
    }

    pub fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
        self.prefix(row2 + 1, col2 + 1)
            - self.prefix(row1, col2 + 1)
            - self.prefix(row2 + 1, col1)
            + self.prefix(row1, col1)
    }
}
