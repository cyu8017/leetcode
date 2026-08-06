// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

impl Solution {
    pub fn nim_game(piles: Vec<i32>) -> bool {
        piles.into_iter().fold(0, |acc, x| acc ^ x) != 0
    }
}
