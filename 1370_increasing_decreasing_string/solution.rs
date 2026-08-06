// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

impl Solution {
    pub fn sort_string(s: String) -> String {
        let mut cnt = [0i32; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut out = String::new();
        while out.len() < s.len() {
            for i in 0..26 {
                if cnt[i] > 0 {
                    out.push((b'a' + i as u8) as char);
                    cnt[i] -= 1;
                }
            }
            for i in (0..26).rev() {
                if cnt[i] > 0 {
                    out.push((b'a' + i as u8) as char);
                    cnt[i] -= 1;
                }
            }
        }
        out
    }
}
