#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

impl Solution {
    pub fn count_divisible_substrings(word: String) -> i32 {
        let vals = [
            1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9,
        ];
        let word = word.as_bytes();
        let n = word.len();
        let mut ans = 0;
        for i in 0..n {
            let mut sum = 0;
            for j in i..n {
                sum += vals[(word[j] - b'a') as usize];
                if sum % (j - i + 1) as i32 == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
