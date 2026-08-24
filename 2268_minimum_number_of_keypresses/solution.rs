// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

impl Solution {
    pub fn minimum_keypresses(s: String) -> i32 {
        let mut freq = [0i32; 26];
        for c in s.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        freq.sort_unstable_by(|a, b| b.cmp(a));
        let mut ans = 0;
        for i in 0..26 {
            if freq[i] == 0 {
                break;
            }
            ans += freq[i] * (i as i32 / 9 + 1);
        }
        ans
    }
}
