// LeetCode 1345 - Jump Game IV
// https://leetcode.com/problems/jump-game-iv/

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut positions: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in arr.iter().enumerate() {
            positions.entry(v).or_default().push(i);
        }
        let mut queue = VecDeque::new();
        let mut seen = HashSet::new();
        queue.push_back(0usize);
        seen.insert(0usize);
        let mut steps = 0;
        while !queue.is_empty() {
            for _ in 0..queue.len() {
                let i = queue.pop_front().unwrap();
                if i == n - 1 {
                    return steps;
                }
                let mut next = positions.remove(&arr[i]).unwrap_or_default();
                next.push(i.wrapping_sub(1));
                next.push(i + 1);
                for j in next {
                    if j < n && seen.insert(j) {
                        queue.push_back(j);
                    }
                }
            }
            steps += 1;
        }
        -1
    }
}
