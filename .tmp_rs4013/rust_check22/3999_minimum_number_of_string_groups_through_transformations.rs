struct Solution;
// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

fn least_rotation(s: &[u8]) -> usize {
    let n = s.len();
    let mut i = 0;
    let mut j = 1;
    let mut k = 0;
    while i < n && j < n && k < n {
        let a = s[(i + k) % n];
        let b = s[(j + k) % n];
        if a == b {
            k += 1;
        } else {
            if a > b {
                i += k + 1;
            } else {
                j += k + 1;
            }
            if i == j {
                j += 1;
            }
            k = 0;
        }
    }
    if i < j {
        i
    } else {
        j
    }
}

fn canonical_rotate(s: String) -> String {
    let n = s.len();
    if n <= 1 {
        return s;
    }
    let r = least_rotation(s.as_bytes());
    if r == 0 {
        return s;
    }
    format!("{}{}", &s[r..], &s[..r])
}

impl Solution {
    pub fn minimum_groups(words: Vec<String>) -> i32 {
        let mut keys = Vec::with_capacity(words.len());
        for w in &words {
            let bytes = w.as_bytes();
            let mut even = String::new();
            let mut odd = String::new();
            for (i, &c) in bytes.iter().enumerate() {
                if i % 2 == 0 {
                    even.push(c as char);
                } else {
                    odd.push(c as char);
                }
            }
            even = canonical_rotate(even);
            odd = canonical_rotate(odd);
            keys.push(format!("{even}#{odd}"));
        }
        keys.sort();
        let mut groups = 0;
        for i in 0..keys.len() {
            if i == 0 || keys[i] != keys[i - 1] {
                groups += 1;
            }
        }
        groups
    }
}

fn main() {}
