// LeetCode 0837 - New 21 Game
// https://leetcode.com/problems/new-21-game/

impl Solution {
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        if k == 0 || n >= k - 1 + max_pts {
            return 1.0;
        }
        let n = n as usize;
        let k = k as usize;
        let max_pts = max_pts as usize;
        let mut dp = vec![0.0; n + 1];
        dp[0] = 1.0;
        let mut window = 1.0;
        let mut ans = 0.0;
        for i in 1..=n {
            dp[i] = window / max_pts as f64;
            if i < k {
                window += dp[i];
            } else {
                ans += dp[i];
            }
            if i >= max_pts && i - max_pts < k {
                window -= dp[i - max_pts];
            }
        }
        ans
    }
}
