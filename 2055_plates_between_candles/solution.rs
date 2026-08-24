// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

impl Solution {
    pub fn plates_between_candles(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let b = s.as_bytes();
        let n = b.len();
        let mut pref = vec![0; n + 1];
        let mut left = vec![0; n];
        let mut right = vec![0; n];
        let mut last = -1;
        for i in 0..n {
            pref[i + 1] = pref[i] + if b[i] == b'*' { 1 } else { 0 };
            if b[i] == b'|' {
                last = i as i32;
            }
            left[i] = last;
        }
        last = -1;
        for i in (0..n).rev() {
            if b[i] == b'|' {
                last = i as i32;
            }
            right[i] = last;
        }
        let mut ans = vec![0; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let l = right[q[0] as usize];
            let r = left[q[1] as usize];
            if l != -1 && r != -1 && l < r {
                ans[i] = pref[r as usize] - pref[l as usize];
            }
        }
        ans
    }
}
