// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

impl Solution {
    pub fn stone_game_viii(mut stones: Vec<i32>) -> i32 {
        let n = stones.len();
        for i in 1..n {
            stones[i] += stones[i - 1];
        }
        let mut score = stones[n - 1];
        for i in (1..n - 1).rev() {
            score = score.max(stones[i] - score);
        }
        score
    }
}
