// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

impl Solution {
    pub fn lexicographically_smallest(n: i32, target: i64) -> Vec<i32> {
        let total = n as i64 * (n as i64 + 1) / 2;
        if target < -total || target > total || (total - target) % 2 != 0 {
            return vec![];
        }
        let mut remaining = (total - target) / 2;
        let mut negative = vec![false; (n + 1) as usize];
        for value in (1..=n).rev() {
            if value as i64 <= remaining {
                negative[value as usize] = true;
                remaining -= value as i64;
            }
        }
        let mut answer = Vec::new();
        for value in (1..=n).rev() {
            if negative[value as usize] {
                answer.push(-value);
            }
        }
        for value in 1..=n {
            if !negative[value as usize] {
                answer.push(value);
            }
        }
        answer
    }
}
