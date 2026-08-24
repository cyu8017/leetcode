// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

impl Solution {
    pub fn employee_free_time(schedule: Vec<Vec<Vec<i32>>>) -> Vec<Vec<i32>> {
        let mut intervals = Vec::new();
        for employee in schedule {
            for item in employee {
                intervals.push(vec![item[0], item[1]]);
            }
        }
        intervals.sort_by_key(|iv| iv[0]);
        let mut merged: Vec<Vec<i32>> = Vec::new();
        for iv in intervals {
            if merged.is_empty() || merged.last().unwrap()[1] < iv[0] {
                merged.push(iv);
            } else {
                let last = merged.last_mut().unwrap();
                last[1] = last[1].max(iv[1]);
            }
        }
        let mut result = Vec::new();
        for i in 1..merged.len() {
            result.push(vec![merged[i - 1][1], merged[i][0]]);
        }
        result
    }
}
