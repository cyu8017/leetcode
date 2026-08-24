// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

impl Solution {
    pub fn maximum_length_substring(s: String) -> i32 {
        let b = s.as_bytes();
        let mut l = 0usize;
        let mut ans = 0i32;
        let mut cnt = [0i32; 26];
        for r in 0..b.len() {
            let idx = (b[r] - b'a') as usize;
            cnt[idx] += 1;
            while cnt[idx] > 2 {
                cnt[(b[l] - b'a') as usize] -= 1;
                l += 1;
            }
            ans = ans.max((r - l + 1) as i32);
        }
        ans
    }
}
