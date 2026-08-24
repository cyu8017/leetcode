// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn sliding_puzzle(board: Vec<Vec<i32>>) -> i32 {
        let mut start = String::new();
        for row in board {
            for cell in row {
                start.push((b'0' + cell as u8) as char);
            }
        }
        let target = "123450";
        let neighbors = [
            vec![1, 3],
            vec![0, 2, 4],
            vec![1, 5],
            vec![0, 4],
            vec![1, 3, 5],
            vec![2, 4],
        ];
        let mut q = VecDeque::new();
        let mut seen = HashSet::new();
        seen.insert(start.clone());
        q.push_back((start, 0));
        while let Some((state, steps)) = q.pop_front() {
            if state == target {
                return steps;
            }
            let zero = state.find('0').unwrap();
            for &nei in &neighbors[zero] {
                let mut nxt: Vec<char> = state.chars().collect();
                nxt.swap(zero, nei);
                let nxt: String = nxt.into_iter().collect();
                if seen.insert(nxt.clone()) {
                    q.push_back((nxt, steps + 1));
                }
            }
        }
        -1
    }
}
