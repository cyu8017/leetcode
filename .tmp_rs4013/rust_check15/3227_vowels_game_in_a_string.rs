struct Solution;
// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

impl Solution {
    pub fn does_alice_win(s: String) -> bool {
        s.chars().any(|c| matches!(c, 'a' | 'e' | 'i' | 'o' | 'u'))
    }
}

fn main() {}
