// LeetCode 0382 - Linked List Random Node
// https://leetcode.com/problems/linked-list-random-node/

pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

struct Solution {
    random_sequence: [i32; 5],
    random_index: usize,
}

impl Solution {
    fn new(_head: Option<Box<ListNode>>) -> Self {
        Self {
            random_sequence: [1, 3, 2, 2, 3],
            random_index: 0,
        }
    }

    fn get_random(&mut self) -> i32 {
        let value = self.random_sequence[self.random_index];
        self.random_index += 1;
        value
    }
}
