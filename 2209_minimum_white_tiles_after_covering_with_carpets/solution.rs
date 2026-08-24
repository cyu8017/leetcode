// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

impl Solution {
    pub fn minimum_white_tiles(floor: String, num_carpets: i32, carpet_len: i32) -> i32 {
        let floor = floor.into_bytes();
        let n = floor.len();
        let num_carpets = num_carpets as usize;
        let carpet_len = carpet_len as usize;
        let inf = 1 << 30;
        let mut dp = vec![vec![inf; n + 1]; num_carpets + 1];
        dp[0][0] = 0;
        for j in 1..=n {
            dp[0][j] = dp[0][j - 1] + i32::from(floor[j - 1] == b'1');
        }
        for c in 1..=num_carpets {
            dp[c][0] = 0;
            for j in 1..=n {
                dp[c][j] = dp[c][j - 1] + i32::from(floor[j - 1] == b'1');
                let start = j.saturating_sub(carpet_len);
                dp[c][j] = dp[c][j].min(dp[c - 1][start]);
            }
        }
        dp[num_carpets][n]
    }
}
