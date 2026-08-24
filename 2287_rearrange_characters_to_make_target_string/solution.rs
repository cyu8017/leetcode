// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

impl Solution {
    pub fn rearrange_characters(s: String, target: String) -> i32 {
        let mut sc = [0i32; 26];
        let mut tc = [0i32; 26];
        for c in s.bytes() {
            sc[(c - b'a') as usize] += 1;
        }
        for c in target.bytes() {
            tc[(c - b'a') as usize] += 1;
        }
        let mut ans = i32::MAX;
        for i in 0..26 {
            if tc[i] == 0 {
                continue;
            }
            ans = ans.min(sc[i] / tc[i]);
        }
        ans
    }
}
