// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

use std::collections::HashMap;

impl Solution {
    pub fn get_hint(secret: String, guess: String) -> String {
        let secret = secret.as_bytes();
        let guess = guess.as_bytes();
        let mut bulls = 0;
        let mut secret_counts: HashMap<u8, i32> = HashMap::new();
        let mut guess_counts: HashMap<u8, i32> = HashMap::new();

        for index in 0..secret.len() {
            if secret[index] == guess[index] {
                bulls += 1;
            } else {
                *secret_counts.entry(secret[index]).or_insert(0) += 1;
                *guess_counts.entry(guess[index]).or_insert(0) += 1;
            }
        }

        let cows = guess_counts
            .iter()
            .map(|(digit, count)| count.min(secret_counts.get(digit).unwrap_or(&0)))
            .sum::<i32>();

        format!("{bulls}A{cows}B")
    }
}
