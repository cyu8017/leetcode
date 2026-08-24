// LeetCode 0920 - Number of Music Playlists
// https://leetcode.com/problems/number-of-music-playlists/

impl Solution {
    pub fn num_music_playlists(n: i32, goal: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let goal = goal as usize;
        let k = k as i64;
        let mut dp = vec![vec![0i64; n + 1]; goal + 1];
        dp[0][0] = 1;
        for i in 1..=goal {
            for j in 1..=i.min(n) {
                dp[i][j] = dp[i - 1][j - 1] * (n as i64 - j as i64 + 1) % MOD;
                if j as i64 > k {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j as i64 - k)) % MOD;
                }
            }
        }
        dp[goal][n] as i32
    }
}
