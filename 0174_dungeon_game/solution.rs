// LeetCode 0174 - Dungeon Game
// https://leetcode.com/problems/dungeon-game/

impl Solution {
    pub fn calculate_minimum_hp(dungeon: Vec<Vec<i32>>) -> i32 {
        let rows = dungeon.len();
        let cols = dungeon[0].len();
        let mut dp = vec![vec![i32::MAX; cols + 1]; rows + 1];
        dp[rows][cols - 1] = 1;
        dp[rows - 1][cols] = 1;

        for row in (0..rows).rev() {
            for col in (0..cols).rev() {
                let need = dp[row + 1][col].min(dp[row][col + 1]) - dungeon[row][col];
                dp[row][col] = need.max(1);
            }
        }
        dp[0][0]
    }
}