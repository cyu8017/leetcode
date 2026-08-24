struct Solution;
// LeetCode 3222 - Find the Winning Player in Coin Game
// https://leetcode.com/problems/find-the-winning-player-in-coin-game/

impl Solution {
    pub fn winning_player(x: i32, y: i32) -> String {
        let k = (x / 2).min(y / 8);
        let x = x - 2 * k;
        let y = y - 8 * k;
        if x > 0 && y >= 4 {
            "Alice".to_string()
        } else {
            "Bob".to_string()
        }
    }
}

fn main() {}
