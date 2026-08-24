// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes();
        let mut ans = 0;
        for i in 0..n {
            let mut cnt = [0i32; 26];
            let mut mx = 0;
            let mut v = 0;
            for j in i..n {
                let c = (bytes[j] - b'a') as usize;
                cnt[c] += 1;
                if cnt[c] == 1 {
                    v += 1;
                }
                mx = mx.max(cnt[c]);
                if mx * v == (j - i + 1) as i32 {
                    ans = ans.max((j - i + 1) as i32);
                }
            }
        }
        ans
    }
}
