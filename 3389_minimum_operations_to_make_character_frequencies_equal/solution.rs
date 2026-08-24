// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

impl Solution {
    pub fn make_string_good(s: String) -> i32 {
        let mut freq = [0i32; 26];
        for c in s.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        let mut ans = s.len() as i32;
        for t in 1..=s.len() as i32 {
            let mut pool = 0;
            for i in 0..26 {
                if freq[i] > t {
                    pool += freq[i] - t;
                }
            }
            let mut deficit = 0;
            for i in 0..26 {
                if freq[i] < t {
                    deficit += t - freq[i];
                }
            }
            let ops = if pool >= deficit { pool } else { deficit };
            if ops < ans {
                ans = ops;
            }
        }
        if (s.len() as i32) < ans {
            ans = s.len() as i32;
        }
        ans
    }
}
