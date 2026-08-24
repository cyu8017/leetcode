// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

impl Solution {
    pub fn xor_game(nums: Vec<i32>) -> bool {
        let x = nums.iter().fold(0, |acc, &num| acc ^ num);
        x == 0 || nums.len() % 2 == 0
    }
}
