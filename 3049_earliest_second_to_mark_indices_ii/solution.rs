// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};

impl Solution {
    fn get_second_to_index(nums: &[i32], change_indices: &[i32]) -> HashMap<i32, usize> {
        let mut index_to_first = HashMap::new();
        for (second, &ci) in change_indices.iter().enumerate() {
            let index = (ci - 1) as usize;
            if nums[index] > 0 {
                index_to_first.entry(index).or_insert(second as i32);
            }
        }
        let mut second_to_index = HashMap::new();
        for (index, second) in index_to_first {
            second_to_index.insert(second, index);
        }
        second_to_index
    }

    fn can_mark(nums: &[i32], second_to_index: &HashMap<i32, usize>, max_second: i32, nums_sum: i64) -> bool {
        let mut h = BinaryHeap::new();
        let mut marks = 0i32;
        for second in (0..max_second).rev() {
            if let Some(&idx) = second_to_index.get(&second) {
                h.push(Reverse(nums[idx]));
                if marks == 0 {
                    h.pop();
                    marks += 1;
                } else {
                    marks -= 1;
                }
            } else {
                marks += 1;
            }
        }
        let heap_size = h.len() as i64;
        let heap_sum: i64 = h.into_iter().map(|Reverse(v)| v as i64).sum();
        let decrement_and_mark = nums_sum - heap_sum + (nums.len() as i64 - heap_size);
        let zero_and_mark = heap_size + heap_size;
        decrement_and_mark + zero_and_mark <= max_second as i64
    }

    pub fn earliest_second_to_mark_indices(nums: Vec<i32>, change_indices: Vec<i32>) -> i32 {
        let second_to_index = Self::get_second_to_index(&nums, &change_indices);
        let nums_sum: i64 = nums.iter().map(|&v| v as i64).sum();
        let mut l = 0i32;
        let mut r = change_indices.len() as i32 + 1;
        while l < r {
            let m = (l + r) / 2;
            if Self::can_mark(&nums, &second_to_index, m, nums_sum) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        if l <= change_indices.len() as i32 { l } else { -1 }
    }
}
