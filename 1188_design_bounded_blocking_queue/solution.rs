// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

use std::collections::VecDeque;
use std::sync::{Condvar, Mutex};

struct BoundedBlockingQueue {
    capacity: usize,
    queue: Mutex<VecDeque<i32>>,
    not_full: Condvar,
    not_empty: Condvar,
}

impl BoundedBlockingQueue {
    fn new(capacity: i32) -> Self {
        Self {
            capacity: capacity as usize,
            queue: Mutex::new(VecDeque::new()),
            not_full: Condvar::new(),
            not_empty: Condvar::new(),
        }
    }

    fn enqueue(&self, element: i32) {
        let mut q = self.queue.lock().unwrap();
        while q.len() == self.capacity {
            q = self.not_full.wait(q).unwrap();
        }
        q.push_back(element);
        self.not_empty.notify_one();
    }

    fn dequeue(&self) -> i32 {
        let mut q = self.queue.lock().unwrap();
        while q.is_empty() {
            q = self.not_empty.wait(q).unwrap();
        }
        let val = q.pop_front().unwrap();
        self.not_full.notify_one();
        val
    }

    fn size(&self) -> i32 {
        self.queue.lock().unwrap().len() as i32
    }
}
