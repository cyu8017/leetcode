struct Solution;
// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

impl Solution {
    pub fn get_words_in_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let n = words.len();
        let mut dp = vec![1i32; n];
        let mut prev = vec![-1i32; n];
        let hamming = |a: &str, b: &str| -> i32 {
            if a.len() != b.len() {
                return 100;
            }
            a.bytes().zip(b.bytes()).filter(|(x, y)| x != y).count() as i32
        };
        let mut best = 1;
        let mut best_i = 0usize;
        for i in 0..n {
            for j in 0..i {
                if groups[i] != groups[j] && hamming(&words[i], &words[j]) == 1 && dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1;
                    prev[i] = j as i32;
                }
            }
            if dp[i] > best {
                best = dp[i];
                best_i = i;
            }
        }
        let mut path = Vec::new();
        let mut i = best_i as i32;
        while i != -1 {
            path.push(words[i as usize].clone());
            i = prev[i as usize];
        }
        path.reverse();
        path
    }
}

fn main() {}
