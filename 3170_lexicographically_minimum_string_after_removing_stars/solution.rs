// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

impl Solution {
    pub fn clear_stars(s: String) -> String {
        let bytes = s.into_bytes();
        let n = bytes.len();
        let mut g: Vec<Vec<usize>> = vec![Vec::new(); 26];
        let mut rem = vec![false; n];
        for i in 0..n {
            if bytes[i] == b'*' {
                rem[i] = true;
                for j in 0..26 {
                    if let Some(idx) = g[j].pop() {
                        rem[idx] = true;
                        break;
                    }
                }
            } else {
                g[(bytes[i] - b'a') as usize].push(i);
            }
        }
        let mut ans = Vec::new();
        for i in 0..n {
            if !rem[i] {
                ans.push(bytes[i]);
            }
        }
        String::from_utf8(ans).unwrap()
    }
}
