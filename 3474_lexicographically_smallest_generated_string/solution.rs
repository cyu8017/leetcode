// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

impl Solution {
    pub fn generate_string(str1: String, str2: String) -> String {
        let n = str1.len();
        let m = str2.len();
        let s1 = str1.as_bytes();
        let s2 = str2.as_bytes();
        let l = n + m - 1;
        let mut ans = vec![b'?'; l];
        for i in 0..n {
            if s1[i] == b'T' {
                for j in 0..m {
                    if ans[i + j] != b'?' && ans[i + j] != s2[j] {
                        return String::new();
                    }
                    ans[i + j] = s2[j];
                }
            }
        }
        for c in ans.iter_mut() {
            if *c == b'?' {
                *c = b'a';
            }
        }
        for i in 0..n {
            if s1[i] == b'F' {
                let mut match_ = true;
                for j in 0..m {
                    if ans[i + j] != s2[j] {
                        match_ = false;
                        break;
                    }
                }
                if match_ {
                    let mut changed = false;
                    for j in (0..m).rev() {
                        let pos = i + j;
                        let mut forced = false;
                        for t in 0..n {
                            if s1[t] == b'T' && pos >= t && pos < t + m {
                                forced = true;
                                break;
                            }
                        }
                        if !forced {
                            ans[pos] = b'b';
                            changed = true;
                            break;
                        }
                    }
                    if !changed {
                        return String::new();
                    }
                }
            }
        }
        for i in 0..n {
            let mut match_ = true;
            for j in 0..m {
                if ans[i + j] != s2[j] {
                    match_ = false;
                    break;
                }
            }
            if s1[i] == b'T' && !match_ {
                return String::new();
            }
            if s1[i] == b'F' && match_ {
                return String::new();
            }
        }
        String::from_utf8(ans).unwrap()
    }
}
