// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

impl Solution {
    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String {
        let n = lcp.len();
        let mut s = vec![0u8; n];
        let mut c = b'a';
        for i in 0..n {
            if s[i] != 0 {
                continue;
            }
            if c > b'z' {
                return String::new();
            }
            s[i] = c;
            for j in i + 1..n {
                if lcp[i][j] > 0 {
                    s[j] = c;
                }
            }
            c += 1;
        }
        for i in (0..n).rev() {
            for j in (0..n).rev() {
                let mut v = 0;
                if s[i] == s[j] {
                    v = 1;
                    if i + 1 < n && j + 1 < n {
                        v += lcp[i + 1][j + 1];
                    }
                }
                if lcp[i][j] != v {
                    return String::new();
                }
            }
        }
        String::from_utf8(s).unwrap()
    }
}
