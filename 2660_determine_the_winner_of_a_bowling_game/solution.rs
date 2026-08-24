// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

impl Solution {
    pub fn is_winner(player1: Vec<i32>, player2: Vec<i32>) -> i32 {
        fn score(p: &[i32]) -> i32 {
            let mut s = 0;
            for i in 0..p.len() {
                let mut mul = 1;
                if (i > 0 && p[i - 1] == 10) || (i > 1 && p[i - 2] == 10) {
                    mul = 2;
                }
                s += mul * p[i];
            }
            s
        }
        let a = score(&player1);
        let b = score(&player2);
        if a > b {
            1
        } else if b > a {
            2
        } else {
            0
        }
    }
}
