// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

struct ZigzagIterator {
    vectors: Vec<Vec<i32>>,
    indices: Vec<usize>,
    turn: usize,
}

impl ZigzagIterator {
    fn new(v1: Vec<i32>, v2: Vec<i32>) -> Self {
        Self {
            vectors: vec![v1, v2],
            indices: vec![0, 0],
            turn: 0,
        }
    }

    fn next(&mut self) -> i32 {
        while self.indices[self.turn] >= self.vectors[self.turn].len() {
            self.turn = 1 - self.turn;
        }
        let value = self.vectors[self.turn][self.indices[self.turn]];
        self.indices[self.turn] += 1;
        self.turn = 1 - self.turn;
        value
    }

    fn has_next(&self) -> bool {
        self.indices
            .iter()
            .enumerate()
            .any(|(index, &position)| position < self.vectors[index].len())
    }
}
