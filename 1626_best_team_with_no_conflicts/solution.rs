// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

impl Solution {
    pub fn best_team_score(scores: Vec<i32>, ages: Vec<i32>) -> i32 {
        let n = scores.len();
        let mut players: Vec<(i32, i32)> = ages.into_iter().zip(scores).collect();
        players.sort_unstable();
        let mut dp = vec![0; n];
        let mut ans = 0;
        for i in 0..n {
            dp[i] = players[i].1;
            for j in 0..i {
                if players[j].1 <= players[i].1 {
                    dp[i] = dp[i].max(dp[j] + players[i].1);
                }
            }
            ans = ans.max(dp[i]);
        }
        ans
    }
}
