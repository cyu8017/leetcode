#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

impl Solution {
    pub fn last_non_empty_string(s: String) -> String {
        let b = s.as_bytes();
        let mut cnt = [0i32; 26];
        let mut last = [0usize; 26];
        let mut mx = 0;
        for (i, &c) in b.iter().enumerate() {
            let ci = (c - b'a') as usize;
            cnt[ci] += 1;
            last[ci] = i;
            mx = mx.max(cnt[ci]);
        }
        let mut ans = String::new();
        for (i, &c) in b.iter().enumerate() {
            let ci = (c - b'a') as usize;
            if cnt[ci] == mx && last[ci] == i {
                ans.push(c as char);
            }
        }
        ans
    }
}
