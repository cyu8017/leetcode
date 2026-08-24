// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

impl Solution {
    pub fn exclusive_time(n: i32, logs: Vec<String>) -> Vec<i32> {
        let mut result = vec![0; n as usize];
        let mut stack = Vec::new();
        let mut prev_time = 0;
        for log in logs {
            let mut parts = log.split(':');
            let func_id: usize = parts.next().unwrap().parse().unwrap();
            let event = parts.next().unwrap();
            let time: i32 = parts.next().unwrap().parse().unwrap();
            if event == "start" {
                if let Some(&top) = stack.last() {
                    result[top] += time - prev_time;
                }
                stack.push(func_id);
                prev_time = time;
            } else {
                let top = stack.pop().unwrap();
                result[top] += time - prev_time + 1;
                prev_time = time + 1;
            }
        }
        result
    }
}
