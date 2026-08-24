// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

pub struct MyCircularDeque {
    data: Vec<i32>,
    capacity: usize,
    front: usize,
    size: usize,
}

impl MyCircularDeque {
    pub fn new(k: i32) -> Self {
        Self {
            data: vec![0; k as usize],
            capacity: k as usize,
            front: 0,
            size: 0,
        }
    }

    pub fn insert_front(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }
        self.front = (self.front + self.capacity - 1) % self.capacity;
        self.data[self.front] = value;
        self.size += 1;
        true
    }

    pub fn insert_last(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }
        self.data[(self.front + self.size) % self.capacity] = value;
        self.size += 1;
        true
    }

    pub fn delete_front(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }
        self.front = (self.front + 1) % self.capacity;
        self.size -= 1;
        true
    }

    pub fn delete_last(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }
        self.size -= 1;
        true
    }

    pub fn get_front(&self) -> i32 {
        if self.is_empty() { -1 } else { self.data[self.front] }
    }

    pub fn get_rear(&self) -> i32 {
        if self.is_empty() {
            -1
        } else {
            self.data[(self.front + self.size - 1) % self.capacity]
        }
    }

    pub fn is_empty(&self) -> bool {
        self.size == 0
    }

    pub fn is_full(&self) -> bool {
        self.size == self.capacity
    }
}
