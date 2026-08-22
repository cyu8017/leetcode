// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn sort_array(nums: Vec<i32>, pre: Vec<i32>) -> i32 {
        let n = nums.len();
        let start = nums.clone();
        let target: Vec<i32> = (0..n as i32).collect();
        if start == target {
            return 0;
        }

        let mut lengths: Vec<usize> = pre
            .into_iter()
            .filter(|&i| i >= 2 && (i as usize) <= n)
            .map(|i| i as usize)
            .collect();
        lengths.sort_unstable();
        lengths.dedup();

        let mut visited: HashSet<Vec<i32>> = HashSet::new();
        visited.insert(start.clone());
        let mut queue: VecDeque<Vec<i32>> = VecDeque::new();
        queue.push_back(start);
        let mut steps = 0;

        while !queue.is_empty() {
            steps += 1;
            for _ in 0..queue.len() {
                let cur = queue.pop_front().unwrap();
                for &i in &lengths {
                    let mut nxt = cur.clone();
                    nxt[..i].reverse();
                    if nxt == target {
                        return steps;
                    }
                    if visited.insert(nxt.clone()) {
                        queue.push_back(nxt);
                    }
                }
            }
        }
        -1
    }
}
