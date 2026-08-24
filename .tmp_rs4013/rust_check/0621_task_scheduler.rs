struct Solution;
// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut counts = [0i32; 26];
        for task in &tasks {
            counts[(*task as u8 - b'A') as usize] += 1;
        }
        let max_freq = *counts.iter().max().unwrap();
        let max_count = counts.iter().filter(|&&c| c == max_freq).count() as i32;
        (tasks.len() as i32).max((max_freq - 1) * (n + 1) + max_count)
    }
}

fn main() {}
