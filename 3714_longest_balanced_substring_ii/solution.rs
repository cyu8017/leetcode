// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

use std::collections::HashMap;

impl Solution {
    fn calc1(s: &[u8]) -> i32 {
        let n = s.len();
        let mut res = 0;
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            while j < n && s[j] == s[i] {
                j += 1;
            }
            res = res.max((j - i) as i32);
            i = j;
        }
        res
    }

    fn calc2(s: &[u8], a: u8, b: u8) -> i32 {
        let n = s.len();
        let mut res = 0;
        let mut i = 0;
        while i < n {
            while i < n && s[i] != a && s[i] != b {
                i += 1;
            }
            let mut pos = HashMap::new();
            pos.insert(0, i as i32 - 1);
            let mut d = 0;
            while i < n && (s[i] == a || s[i] == b) {
                if s[i] == a {
                    d += 1;
                } else {
                    d -= 1;
                }
                if let Some(&p) = pos.get(&d) {
                    res = res.max(i as i32 - p);
                } else {
                    pos.insert(d, i as i32);
                }
                i += 1;
            }
        }
        res
    }

    fn calc3(s: &[u8]) -> i32 {
        let mut pos = HashMap::new();
        pos.insert((0, 0), -1);
        let mut cnt = [0i32; 3];
        let mut res = 0;
        for (i, &c) in s.iter().enumerate() {
            cnt[(c - b'a') as usize] += 1;
            let x = cnt[0] - cnt[1];
            let y = cnt[1] - cnt[2];
            if let Some(&p) = pos.get(&(x, y)) {
                res = res.max(i as i32 - p);
            } else {
                pos.insert((x, y), i as i32);
            }
        }
        res
    }

    pub fn longest_balanced(s: String) -> i32 {
        let s = s.as_bytes();
        let x = Self::calc1(s);
        let y = Self::calc2(s, b'a', b'b')
            .max(Self::calc2(s, b'b', b'c'))
            .max(Self::calc2(s, b'a', b'c'));
        let z = Self::calc3(s);
        x.max(y).max(z)
    }
}
