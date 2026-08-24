struct Solution;

// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

impl Solution {
    pub fn minimum_score(s: String, t: String) -> i32 {
        let s = s.as_bytes();
        let t = t.as_bytes();
        let n = s.len();
        let m = t.len();
        let mut left = vec![-1i32; m];
        let mut right = vec![-1i32; m];
        let mut j = 0;
        for i in 0..n {
            if j < m && s[i] == t[j] {
                left[j] = i as i32;
                j += 1;
            }
        }
        j = m;
        for i in (0..n).rev() {
            if j > 0 && s[i] == t[j - 1] {
                right[j - 1] = i as i32;
                j -= 1;
            }
        }
        if m > 0 && left[m - 1] != -1 {
            return 0;
        }
        let mut ans = m as i32;
        for i in 0..m {
            if right[i] != -1 {
                if i as i32 + 0 < ans {
                    ans = i as i32;
                }
                break;
            }
        }
        for i in (0..m).rev() {
            if left[i] != -1 {
                let rem = (m - 1 - i) as i32;
                if rem < ans {
                    ans = rem;
                }
                break;
            }
        }
        let mut j = 0;
        for i in 0..m {
            if left[i] == -1 {
                break;
            }
            while j < m && (right[j] == -1 || right[j] <= left[i]) {
                j += 1;
            }
            if j < m {
                let rem = j as i32 - i as i32 - 1;
                if rem < ans {
                    ans = rem;
                }
            }
        }
        ans
    }
}

fn main() {}
