// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

pub struct MyLinkedList {
    data: Vec<i32>,
}

impl MyLinkedList {
    pub fn new() -> Self {
        Self { data: Vec::new() }
    }

    pub fn get(&self, index: i32) -> i32 {
        self.data.get(index as usize).copied().unwrap_or(-1)
    }

    pub fn add_at_head(&mut self, val: i32) {
        self.add_at_index(0, val);
    }

    pub fn add_at_tail(&mut self, val: i32) {
        self.add_at_index(self.data.len() as i32, val);
    }

    pub fn add_at_index(&mut self, index: i32, val: i32) {
        let index = index as usize;
        if index > self.data.len() {
            return;
        }
        self.data.insert(index, val);
    }

    pub fn delete_at_index(&mut self, index: i32) {
        let index = index as usize;
        if index < self.data.len() {
            self.data.remove(index);
        }
    }
}
