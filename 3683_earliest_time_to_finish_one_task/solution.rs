// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

impl Solution {
    pub fn earliest_time(tasks: Vec<Vec<i32>>) -> i32 {
        let mut ans = 200;
        for task in tasks {
            ans = ans.min(task[0] + task[1]);
        }
        ans
    }
}
