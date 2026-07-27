// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

impl Solution {
    pub fn stone_game_vii(stones: Vec<i32>) -> i32 {
        let n = stones.len();
        let mut pre = vec![0i32; n + 1];
        for i in 0..n {
            pre[i + 1] = pre[i] + stones[i];
        }
        let mut dp = vec![vec![0i32; n]; n];
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                dp[i][j] = (pre[j + 1] - pre[i + 1] - dp[i + 1][j])
                    .max(pre[j] - pre[i] - dp[i][j - 1]);
            }
        }
        dp[0][n - 1]
    }
}
