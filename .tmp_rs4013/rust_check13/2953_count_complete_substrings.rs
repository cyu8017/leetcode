#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

impl Solution {
    pub fn count_complete_substrings(word: String, k: i32) -> i32 {
        let word = word.as_bytes();
        let n = word.len();
        let mut ans = 0;
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j + 1 < n && (word[j + 1] as i32 - word[j] as i32).abs() <= 2 {
                j += 1;
            }
            let seg = &word[i..=j];
            let m = seg.len();
            for chars in 1..=26 {
                let length = chars * k as usize;
                if length > m {
                    break;
                }
                let mut freq = [0i32; 26];
                let mut unique = 0;
                for r in 0..m {
                    let c = (seg[r] - b'a') as usize;
                    freq[c] += 1;
                    if freq[c] == 1 {
                        unique += 1;
                    }
                    if r >= length {
                        let c2 = (seg[r - length] - b'a') as usize;
                        freq[c2] -= 1;
                        if freq[c2] == 0 {
                            unique -= 1;
                        }
                    }
                    if r >= length - 1 && unique == chars {
                        let ok = freq.iter().all(|&f| f == 0 || f == k);
                        if ok {
                            ans += 1;
                        }
                    }
                }
            }
            i = j + 1;
        }
        ans
    }
}
