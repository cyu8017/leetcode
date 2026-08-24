// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

impl Solution {
    pub fn maximum_length(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut ans = -1;
        for i in 0..n {
            for j in i..n {
                if b[j] != b[i] {
                    break;
                }
                let len = j - i + 1;
                let mut cnt = 0;
                for k in 0..=n.saturating_sub(len) {
                    if &b[k..k + len] == &b[i..i + len] {
                        cnt += 1;
                    }
                }
                if cnt >= 3 && len as i32 > ans {
                    ans = len as i32;
                }
            }
        }
        ans
    }
}
