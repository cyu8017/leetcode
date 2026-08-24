// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

impl Solution {
    pub fn match_players_and_trainers(mut players: Vec<i32>, mut trainers: Vec<i32>) -> i32 {
        players.sort_unstable();
        trainers.sort_unstable();
        let mut i = 0;
        let mut j = 0;
        let mut ans = 0;
        while i < players.len() && j < trainers.len() {
            if players[i] <= trainers[j] {
                ans += 1;
                i += 1;
                j += 1;
            } else {
                j += 1;
            }
        }
        ans
    }
}
