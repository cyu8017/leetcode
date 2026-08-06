// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn max_candies(
        mut status: Vec<i32>,
        candies: Vec<i32>,
        keys: Vec<Vec<i32>>,
        contained_boxes: Vec<Vec<i32>>,
        initial_boxes: Vec<i32>,
    ) -> i32 {
        let mut owned = HashSet::new();
        let mut opened = HashSet::new();
        let mut q = VecDeque::new();
        for box_id in initial_boxes {
            owned.insert(box_id);
            if status[box_id as usize] == 1 {
                q.push_back(box_id);
            }
        }
        let mut total = 0;
        while let Some(box_id) = q.pop_front() {
            let b = box_id as usize;
            if opened.contains(&box_id) || status[b] == 0 {
                continue;
            }
            opened.insert(box_id);
            total += candies[b];
            for &key in &keys[b] {
                status[key as usize] = 1;
                if owned.contains(&key) && !opened.contains(&key) {
                    q.push_back(key);
                }
            }
            for &child in &contained_boxes[b] {
                owned.insert(child);
                if status[child as usize] == 1 && !opened.contains(&child) {
                    q.push_back(child);
                }
            }
        }
        total
    }
}
