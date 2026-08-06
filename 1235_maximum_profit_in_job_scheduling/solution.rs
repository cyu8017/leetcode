// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

impl Solution {
    pub fn job_scheduling(start_time: Vec<i32>, end_time: Vec<i32>, profit: Vec<i32>) -> i32 {
        let n = start_time.len();
        let mut jobs: Vec<(i32, i32, i32)> = (0..n)
            .map(|i| (end_time[i], start_time[i], profit[i]))
            .collect();
        jobs.sort_unstable();
        let mut ends = vec![0];
        let mut dp = vec![0];
        for (end, start, gain) in jobs {
            let i = ends.partition_point(|&e| e <= start) - 1;
            let best = dp.last().unwrap().max(&(dp[i] + gain));
            ends.push(end);
            dp.push(best);
        }
        *dp.last().unwrap()
    }
}
