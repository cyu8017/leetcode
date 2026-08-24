// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

pub struct ExamTracker {
    times: Vec<i32>,
    pre: Vec<i64>,
}

impl ExamTracker {
    pub fn new() -> Self {
        Self {
            times: vec![0],
            pre: vec![0],
        }
    }

    pub fn record(&mut self, time: i32, score: i32) {
        self.times.push(time);
        self.pre.push(self.pre.last().copied().unwrap() + score as i64);
    }

    pub fn total_score(&self, start_time: i32, end_time: i32) -> i64 {
        let l = self.times.partition_point(|&t| t < start_time) as i32 - 1;
        let r = self.times.partition_point(|&t| t < end_time + 1) as i32 - 1;
        self.pre[r as usize] - self.pre[l as usize]
    }
}
