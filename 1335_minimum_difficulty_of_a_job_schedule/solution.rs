// LeetCode 1335 - Minimum Difficulty of a Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

impl Solution {
    pub fn min_difficulty(job_difficulty: Vec<i32>, d: i32) -> i32 {
        let n = job_difficulty.len();
        let d = d as usize;
        if n < d {
            return -1;
        }
        let mut dp = vec![i32::MAX / 2; n];
        let mut hardest = 0;
        for i in 0..n {
            hardest = hardest.max(job_difficulty[i]);
            dp[i] = hardest;
        }
        for day in 1..d {
            let mut nxt = vec![i32::MAX / 2; n];
            for end in day..n {
                let mut hardest = 0;
                for start in (day..=end).rev() {
                    hardest = hardest.max(job_difficulty[start]);
                    nxt[end] = nxt[end].min(dp[start - 1] + hardest);
                }
            }
            dp = nxt;
        }
        dp[n - 1]
    }
}
