// LeetCode 0432 - All O`one` Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

use std::collections::{HashMap, HashSet};

struct Bucket {
    count: i32,
    keys: HashSet<String>,
    prev: usize,
    next: usize,
}

pub struct AllOne {
    nodes: Vec<Bucket>,
    head: usize,
    tail: usize,
    key_nodes: HashMap<String, usize>,
}

impl AllOne {
    pub fn new() -> Self {
        let mut nodes = Vec::new();
        nodes.push(Bucket {
            count: 0,
            keys: HashSet::new(),
            prev: 0,
            next: 1,
        });
        nodes.push(Bucket {
            count: 0,
            keys: HashSet::new(),
            prev: 0,
            next: 1,
        });
        Self {
            nodes,
            head: 0,
            tail: 1,
            key_nodes: HashMap::new(),
        }
    }

    fn insert_after(&mut self, anchor: usize, node_index: usize) {
        let next = self.nodes[anchor].next;
        self.nodes[node_index].prev = anchor;
        self.nodes[node_index].next = next;
        self.nodes[anchor].next = node_index;
        self.nodes[next].prev = node_index;
    }

    fn remove_bucket(&mut self, node_index: usize) {
        let previous = self.nodes[node_index].prev;
        let next = self.nodes[node_index].next;
        self.nodes[previous].next = next;
        self.nodes[next].prev = previous;
    }

    fn ensure_count_node(&mut self, count: i32, after: usize) -> usize {
        let mut current = self.nodes[after].next;
        while current != self.tail && self.nodes[current].count < count {
            current = self.nodes[current].next;
        }
        if current != self.tail && self.nodes[current].count == count {
            return current;
        }

        let previous = self.nodes[current].prev;
        let node_index = self.nodes.len();
        self.nodes.push(Bucket {
            count,
            keys: HashSet::new(),
            prev: 0,
            next: 0,
        });
        self.insert_after(previous, node_index);
        node_index
    }

    pub fn inc(&mut self, key: String) {
        if let Some(&bucket_index) = self.key_nodes.get(&key) {
            self.nodes[bucket_index].keys.remove(&key);
            let next_bucket = self.ensure_count_node(self.nodes[bucket_index].count + 1, bucket_index);
            self.nodes[next_bucket].keys.insert(key.clone());
            self.key_nodes.insert(key, next_bucket);
            if self.nodes[bucket_index].keys.is_empty() {
                self.remove_bucket(bucket_index);
            }
            return;
        }

        let bucket = self.ensure_count_node(1, self.head);
        self.nodes[bucket].keys.insert(key.clone());
        self.key_nodes.insert(key, bucket);
    }

    pub fn dec(&mut self, key: String) {
        let bucket_index = self.key_nodes[&key];
        self.nodes[bucket_index].keys.remove(&key);
        if self.nodes[bucket_index].count == 1 {
            self.key_nodes.remove(&key);
        } else {
            let prev_bucket = self.ensure_count_node(self.nodes[bucket_index].count - 1, self.head);
            self.nodes[prev_bucket].keys.insert(key.clone());
            self.key_nodes.insert(key, prev_bucket);
        }
        if self.nodes[bucket_index].keys.is_empty() {
            self.remove_bucket(bucket_index);
        }
    }

    pub fn get_max_key(&self) -> String {
        let bucket = self.nodes[self.tail].prev;
        if bucket == self.head {
            return String::new();
        }
        self.nodes[bucket].keys.iter().next().cloned().unwrap_or_default()
    }

    pub fn get_min_key(&self) -> String {
        let bucket = self.nodes[self.head].next;
        if bucket == self.tail {
            return String::new();
        }
        self.nodes[bucket].keys.iter().next().cloned().unwrap_or_default()
    }
}
