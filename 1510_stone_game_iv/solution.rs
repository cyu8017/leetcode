// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

impl Solution {
    pub fn winner_square_game(n: i32) -> bool {
        let n = n as usize;
        let mut win = vec![false; n + 1];
        for value in 1..=n {
            let mut root = 1;
            while root * root <= value {
                if !win[value - root * root] {
                    win[value] = true;
                    break;
                }
                root += 1;
            }
        }
        win[n]
    }
}
