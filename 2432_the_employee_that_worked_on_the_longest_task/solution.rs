// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

impl Solution {
    pub fn hardest_worker(_n: i32, logs: Vec<Vec<i32>>) -> i32 {
        let mut ans = logs[0][0];
        let mut best = logs[0][1];
        let mut prev = 0;
        for log in &logs {
            let dur = log[1] - prev;
            if dur > best || (dur == best && log[0] < ans) {
                best = dur;
                ans = log[0];
            }
            prev = log[1];
        }
        ans
    }
}
