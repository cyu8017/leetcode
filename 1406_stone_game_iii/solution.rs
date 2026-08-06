// LeetCode 1406 - Stone Game III
// https://leetcode.com/problems/stone-game-iii/

impl Solution {
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        let n = stone_value.len();
        let mut dp = vec![0i64; n + 1];
        for i in (0..n).rev() {
            let mut take = 0i64;
            dp[i] = i64::MIN / 4;
            for j in i..n.min(i + 3) {
                take += stone_value[j] as i64;
                dp[i] = dp[i].max(take - dp[j + 1]);
            }
        }
        if dp[0] > 0 {
            "Alice".to_string()
        } else if dp[0] < 0 {
            "Bob".to_string()
        } else {
            "Tie".to_string()
        }
    }
}
