// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

impl Solution {
    pub fn super_egg_drop(k: i32, n: i32) -> i32 {
        let k = k as usize;
        let mut dp = vec![0i32; k + 1];
        let mut moves = 0;
        while dp[k] < n {
            moves += 1;
            for eggs in (1..=k).rev() {
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1;
            }
        }
        moves
    }
}
