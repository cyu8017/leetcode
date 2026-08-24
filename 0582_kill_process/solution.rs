// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn kill_process(pid: Vec<i32>, ppid: Vec<i32>, kill: i32) -> Vec<i32> {
        let mut children: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..pid.len() {
            children.entry(ppid[i]).or_default().push(pid[i]);
        }
        let mut result = Vec::new();
        let mut queue = VecDeque::new();
        queue.push_back(kill);
        while let Some(process) = queue.pop_front() {
            result.push(process);
            if let Some(kids) = children.get(&process) {
                for &child in kids {
                    queue.push_back(child);
                }
            }
        }
        result
    }
}
