// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

use std::collections::HashMap;

impl Solution {
    pub fn possibly_equals(s1: String, s2: String) -> bool {
        let a = s1.as_bytes();
        let b = s2.as_bytes();
        fn is_digit(c: u8) -> bool {
            c.is_ascii_digit()
        }
        fn dfs(
            i: usize,
            j: usize,
            diff: i32,
            a: &[u8],
            b: &[u8],
            memo: &mut HashMap<(usize, usize, i32), bool>,
        ) -> bool {
            let key = (i, j, diff);
            if let Some(&v) = memo.get(&key) {
                return v;
            }
            let n = a.len();
            let m = b.len();
            if i == n && j == m {
                memo.insert(key, diff == 0);
                return diff == 0;
            }
            let mut res = false;
            if diff == 0 && i < n && j < m && !is_digit(a[i]) && !is_digit(b[j]) {
                if a[i] == b[j] {
                    res = dfs(i + 1, j + 1, 0, a, b, memo);
                }
            } else if diff > 0 && i < n && !is_digit(a[i]) {
                res = dfs(i + 1, j, diff - 1, a, b, memo);
            } else if diff < 0 && j < m && !is_digit(b[j]) {
                res = dfs(i, j + 1, diff + 1, a, b, memo);
            }
            if !res && i < n && is_digit(a[i]) {
                let mut val = 0;
                let mut p = i;
                while p < n && is_digit(a[p]) {
                    val = val * 10 + (a[p] - b'0') as i32;
                    if dfs(p + 1, j, diff + val, a, b, memo) {
                        res = true;
                        break;
                    }
                    p += 1;
                }
            }
            if !res && j < m && is_digit(b[j]) {
                let mut val = 0;
                let mut p = j;
                while p < m && is_digit(b[p]) {
                    val = val * 10 + (b[p] - b'0') as i32;
                    if dfs(i, p + 1, diff - val, a, b, memo) {
                        res = true;
                        break;
                    }
                    p += 1;
                }
            }
            memo.insert(key, res);
            res
        }
        let mut memo = HashMap::new();
        dfs(0, 0, 0, a, b, &mut memo)
    }
}
