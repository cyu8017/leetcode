// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

use std::collections::BinaryHeap;

impl Solution {
    pub fn find_maximized_capital(k: i32, mut w: i32, mut profits: Vec<i32>, mut capital: Vec<i32>) -> i32 {
        let mut projects: Vec<(i32, i32)> = capital.drain(..).zip(profits.drain(..)).collect();
        projects.sort_unstable_by_key(|project| project.0);

        let mut available = BinaryHeap::new();
        let mut index = 0;
        for _ in 0..k {
            while index < projects.len() && projects[index].0 <= w {
                available.push(projects[index].1);
                index += 1;
            }
            if let Some(profit) = available.pop() {
                w += profit;
            } else {
                break;
            }
        }
        w
    }
}
