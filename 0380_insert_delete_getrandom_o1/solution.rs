// LeetCode 0380 - Insert Delete GetRandom O(1)
// https://leetcode.com/problems/insert-delete-getrandom-o1/

use rand::Rng;
use std::collections::HashMap;

struct RandomizedSet {
    values: Vec<i32>,
    index_by_value: HashMap<i32, usize>,
}

impl RandomizedSet {
    fn new() -> Self {
        Self {
            values: Vec::new(),
            index_by_value: HashMap::new(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        if self.index_by_value.contains_key(&val) {
            return false;
        }
        self.index_by_value.insert(val, self.values.len());
        self.values.push(val);
        true
    }

    fn remove(&mut self, val: i32) -> bool {
        let index = match self.index_by_value.get(&val) {
            Some(value) => *value,
            None => return false,
        };

        let last_value = *self.values.last().unwrap();
        self.values[index] = last_value;
        self.index_by_value.insert(last_value, index);
        self.values.pop();
        self.index_by_value.remove(&val);
        true
    }

    fn get_random(&self) -> i32 {
        let index = rand::thread_rng().gen_range(0..self.values.len());
        self.values[index]
    }
}
