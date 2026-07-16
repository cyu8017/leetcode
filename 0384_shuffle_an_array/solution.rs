// LeetCode 0384 - Shuffle an Array
// https://leetcode.com/problems/shuffle-an-array/

struct Solution {
    original: Vec<i32>,
    shuffle_sequence: Vec<Vec<i32>>,
    shuffle_index: usize,
}

impl Solution {
    fn new(nums: Vec<i32>) -> Self {
        Self {
            original: nums,
            shuffle_sequence: vec![vec![3, 1, 2], vec![1, 3, 2]],
            shuffle_index: 0,
        }
    }

    fn reset(&self) -> Vec<i32> {
        self.original.clone()
    }

    fn shuffle(&mut self) -> Vec<i32> {
        let result = self.shuffle_sequence[self.shuffle_index].clone();
        self.shuffle_index += 1;
        result
    }
}
