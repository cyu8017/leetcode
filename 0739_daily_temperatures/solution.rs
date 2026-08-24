// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n = temperatures.len();
        let mut answer = vec![0; n];
        let mut stack = Vec::new();
        for i in 0..n {
            while let Some(&prev) = stack.last() {
                if temperatures[prev] < temperatures[i] {
                    stack.pop();
                    answer[prev] = (i - prev) as i32;
                } else {
                    break;
                }
            }
            stack.push(i);
        }
        answer
    }
}
