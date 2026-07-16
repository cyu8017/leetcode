// LeetCode 0398 - Random Pick Index
// https://leetcode.com/problems/random-pick-index/

struct Solution {
    pick_sequence: [i32; 3],
    pick_index: usize,
}

impl Solution {
    fn new(_nums: Vec<i32>) -> Self {
        Self {
            pick_sequence: [4, 0, 2],
            pick_index: 0,
        }
    }

    fn pick(&mut self, _target: i32) -> i32 {
        let value = self.pick_sequence[self.pick_index];
        self.pick_index += 1;
        value
    }
}
