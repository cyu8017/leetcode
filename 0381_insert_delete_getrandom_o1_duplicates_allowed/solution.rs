// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

use std::collections::{HashMap, HashSet};

struct RandomizedCollection {
    values: Vec<i32>,
    indices_by_value: HashMap<i32, HashSet<usize>>,
}

impl RandomizedCollection {
    fn new() -> Self {
        Self {
            values: Vec::new(),
            indices_by_value: HashMap::new(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        self.indices_by_value
            .entry(val)
            .or_default()
            .insert(self.values.len());
        self.values.push(val);
        self.indices_by_value.get(&val).unwrap().len() == 1
    }

    fn remove(&mut self, val: i32) -> bool {
        let index = match self.indices_by_value.get_mut(&val) {
            Some(indices) if !indices.is_empty() => *indices.iter().next().unwrap(),
            _ => return false,
        };

        let last_index = self.values.len() - 1;
        let last_value = self.values[last_index];
        self.values[index] = last_value;

        if let Some(indices) = self.indices_by_value.get_mut(&last_value) {
            indices.remove(&last_index);
            indices.insert(index);
        }

        self.values.pop();

        if let Some(indices) = self.indices_by_value.get_mut(&val) {
            indices.remove(&index);
            if indices.is_empty() {
                self.indices_by_value.remove(&val);
            }
        }

        true
    }

    fn get_random(&self) -> i32 {
        *self.values.last().unwrap()
    }
}
