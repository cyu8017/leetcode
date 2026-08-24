// LeetCode 3104 - Find Longest Self-Contained Substring
// https://leetcode.com/problems/find-longest-self-contained-substring/

impl Solution {
    pub fn max_substring_length(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut first = [-1i32; 26];
        let mut last = [0i32; 26];
        for i in 0..n {
            let j = (b[i] - b'a') as usize;
            if first[j] == -1 {
                first[j] = i as i32;
            }
            last[j] = i as i32;
        }
        let mut ans = -1i32;
        for k in 0..26 {
            let i = first[k];
            if i == -1 {
                continue;
            }
            let mut mx = last[k];
            for j in i as usize..n {
                let a = first[(b[j] - b'a') as usize];
                let bb = last[(b[j] - b'a') as usize];
                if a < i {
                    break;
                }
                mx = mx.max(bb);
                if mx == j as i32 && (j as i32 - i + 1) < n as i32 {
                    ans = ans.max(j as i32 - i + 1);
                }
            }
        }
        ans
    }
}
