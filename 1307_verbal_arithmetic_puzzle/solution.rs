// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn is_solvable(words: Vec<String>, result: String) -> bool {
        if words.iter().map(|w| w.len()).max().unwrap_or(0) > result.len() {
            return false;
        }
        let mut letters: HashSet<char> = HashSet::new();
        for w in &words {
            letters.extend(w.chars());
        }
        letters.extend(result.chars());
        if letters.len() > 10 {
            return false;
        }
        let mut leading = HashSet::new();
        for w in words.iter().chain(std::iter::once(&result)) {
            if w.len() > 1 {
                leading.insert(w.chars().next().unwrap());
            }
        }
        let words: Vec<Vec<char>> = words.into_iter().map(|w| w.chars().collect()).collect();
        let result: Vec<char> = result.chars().collect();
        let width = result.len();
        let mut value: HashMap<char, i32> = HashMap::new();
        let mut used = [false; 10];

        fn solve(
            column: usize,
            row: usize,
            total: i32,
            words: &[Vec<char>],
            result: &[char],
            width: usize,
            leading: &HashSet<char>,
            value: &mut HashMap<char, i32>,
            used: &mut [bool; 10],
        ) -> bool {
            if column == width {
                return total == 0;
            }
            if row < words.len() {
                if column >= words[row].len() {
                    return solve(column, row + 1, total, words, result, width, leading, value, used);
                }
                let ch = words[row][words[row].len() - 1 - column];
                if let Some(&digit) = value.get(&ch) {
                    return solve(column, row + 1, total + digit, words, result, width, leading, value, used);
                }
                for digit in 0..10 {
                    if !used[digit as usize] && (digit != 0 || !leading.contains(&ch)) {
                        value.insert(ch, digit);
                        used[digit as usize] = true;
                        if solve(column, row + 1, total + digit, words, result, width, leading, value, used) {
                            return true;
                        }
                        used[digit as usize] = false;
                        value.remove(&ch);
                    }
                }
                return false;
            }
            let ch = result[result.len() - 1 - column];
            let digit = total % 10;
            let carry = total / 10;
            if let Some(&mapped) = value.get(&ch) {
                return mapped == digit
                    && solve(column + 1, 0, carry, words, result, width, leading, value, used);
            }
            if used[digit as usize] || (digit == 0 && leading.contains(&ch)) {
                return false;
            }
            value.insert(ch, digit);
            used[digit as usize] = true;
            let ok = solve(column + 1, 0, carry, words, result, width, leading, value, used);
            used[digit as usize] = false;
            value.remove(&ch);
            ok
        }

        solve(0, 0, 0, &words, &result, width, &leading, &mut value, &mut used)
    }
}
