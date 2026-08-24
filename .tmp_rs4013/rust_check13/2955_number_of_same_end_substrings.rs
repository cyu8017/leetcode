#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

impl Solution {
    pub fn same_end_substring_count(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let s = s.as_bytes();
        let n = s.len();
        let mut pref = vec![[0i32; 26]; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i];
            pref[i + 1][(s[i] - b'a') as usize] += 1;
        }
        let mut ans = vec![0; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let mut total = 0;
            for c in 0..26 {
                let cnt = pref[r + 1][c] - pref[l][c];
                total += cnt * (cnt + 1) / 2;
            }
            ans[qi] = total;
        }
        ans
    }
}
