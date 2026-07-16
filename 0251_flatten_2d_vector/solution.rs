// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

struct Vector2D {
    vec: Vec<Vec<i32>>,
    row: usize,
    col: usize,
}

impl Vector2D {
    fn new(vec: Vec<Vec<i32>>) -> Self {
        let mut iterator = Self { vec, row: 0, col: 0 };
        iterator.advance();
        iterator
    }

    fn advance(&mut self) {
        while self.row < self.vec.len() && self.col >= self.vec[self.row].len() {
            self.row += 1;
            self.col = 0;
        }
    }

    fn next(&mut self) -> i32 {
        let value = self.vec[self.row][self.col];
        self.col += 1;
        self.advance();
        value
    }

    fn has_next(&mut self) -> bool {
        self.advance();
        self.row < self.vec.len()
    }
}
