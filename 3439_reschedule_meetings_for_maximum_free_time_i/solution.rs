// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

impl Solution {
    pub fn max_free_time(
        event_time: i32,
        k: i32,
        start_time: Vec<i32>,
        end_time: Vec<i32>,
    ) -> i32 {
        let n = start_time.len();
        let mut gaps = vec![0; n + 1];
        gaps[0] = start_time[0];
        for i in 1..n {
            gaps[i] = start_time[i] - end_time[i - 1];
        }
        gaps[n] = event_time - end_time[n - 1];
        let window = (k + 1) as usize;
        let mut sum = 0;
        for i in 0..window.min(gaps.len()) {
            sum += gaps[i];
        }
        let mut ans = sum;
        for i in window..gaps.len() {
            sum += gaps[i] - gaps[i - window];
            if sum > ans {
                ans = sum;
            }
        }
        ans
    }
}
