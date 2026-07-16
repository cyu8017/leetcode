// LeetCode 0146 - LRU Cache
// https://leetcode.com/problems/lru-cache/

// LeetCode 0146 - LRU Cache
// https://leetcode.com/problems/lru-cache/

use std::collections::HashMap;

struct Node {
    key: i32,
    value: i32,
    prev: usize,
    next: usize,
}

pub struct LRUCache {
    capacity: usize,
    nodes: Vec<Node>,
    locations: HashMap<i32, usize>,
}

impl LRUCache {
    pub fn new(capacity: i32) -> Self {
        let mut nodes = Vec::new();
        nodes.push(Node { key: 0, value: 0, prev: 0, next: 1 });
        nodes.push(Node { key: 0, value: 0, prev: 0, next: 1 });
        Self { capacity: capacity.max(0) as usize, nodes, locations: HashMap::new() }
    }

    fn unlink(&mut self, index: usize) {
        let previous = self.nodes[index].prev;
        let next = self.nodes[index].next;
        self.nodes[previous].next = next;
        self.nodes[next].prev = previous;
    }

    fn add_front(&mut self, index: usize) {
        let first = self.nodes[0].next;
        self.nodes[index].prev = 0;
        self.nodes[index].next = first;
        self.nodes[0].next = index;
        self.nodes[first].prev = index;
    }

    pub fn get(&mut self, key: i32) -> i32 {
        let Some(&index) = self.locations.get(&key) else { return -1; };
        self.unlink(index);
        self.add_front(index);
        self.nodes[index].value
    }

    pub fn put(&mut self, key: i32, value: i32) {
        if let Some(&index) = self.locations.get(&key) {
            self.nodes[index].value = value;
            self.unlink(index);
            self.add_front(index);
            return;
        }
        if self.capacity == 0 {
            return;
        }
        if self.locations.len() == self.capacity {
            let least_recent = self.nodes[1].prev;
            let old_key = self.nodes[least_recent].key;
            self.unlink(least_recent);
            self.locations.remove(&old_key);
        }
        let index = self.nodes.len();
        self.nodes.push(Node { key, value, prev: 0, next: 0 });
        self.add_front(index);
        self.locations.insert(key, index);
    }
}