// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

impl Solution {
    pub fn max_free_time(event_time: i32, start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        let n = start_time.len();
        let mut gaps = vec![0; n + 1];
        gaps[0] = start_time[0];
        for i in 1..n {
            gaps[i] = start_time[i] - end_time[i - 1];
        }
        gaps[n] = event_time - end_time[n - 1];
        let mut ans = 0;
        for &g in &gaps {
            if g > ans {
                ans = g;
            }
        }
        let mut left_max = vec![0; n + 1];
        let mut right_max = vec![0; n + 1];
        for i in 0..=n {
            left_max[i] = gaps[i];
            if i > 0 && left_max[i - 1] > left_max[i] {
                left_max[i] = left_max[i - 1];
            }
        }
        for i in (0..=n).rev() {
            right_max[i] = gaps[i];
            if i < n && right_max[i + 1] > right_max[i] {
                right_max[i] = right_max[i + 1];
            }
        }
        for i in 0..n {
            let dur = end_time[i] - start_time[i];
            let merged = gaps[i] + gaps[i + 1];
            let mut best_other = 0;
            if i > 0 && left_max[i - 1] > best_other {
                best_other = left_max[i - 1];
            }
            if i + 2 <= n && right_max[i + 2] > best_other {
                best_other = right_max[i + 2];
            }
            let mut cand = merged;
            if best_other >= dur {
                cand = merged + dur;
            }
            if cand > ans {
                ans = cand;
            }
        }
        ans
    }
}
