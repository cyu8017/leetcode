// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

impl Solution {
    pub fn min_sessions(tasks: Vec<i32>, session_time: i32) -> i32 {
        let n = tasks.len();
        let inf = (n as i32 + 1, 0i32);
        let mut dp = vec![inf; 1 << n];
        dp[0] = (1, 0);
        for mask in 0..(1 << n) {
            let (sessions, used) = dp[mask];
            if sessions > n as i32 {
                continue;
            }
            for i in 0..n {
                if mask & (1 << i) != 0 {
                    continue;
                }
                let t = tasks[i];
                let nmask = mask | (1 << i);
                let cand = if used + t <= session_time {
                    (sessions, used + t)
                } else {
                    (sessions + 1, t)
                };
                if cand < dp[nmask] {
                    dp[nmask] = cand;
                }
            }
        }
        dp[(1 << n) - 1].0
    }
}
