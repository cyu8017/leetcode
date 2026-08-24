// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

use std::collections::HashMap;

impl Solution {
    pub fn substring_xor_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let s = s.as_bytes();
        let n = s.len();
        let mut pos: HashMap<i32, (i32, i32)> = HashMap::new();
        for i in 0..n {
            if s[i] == b'0' {
                pos.entry(0).or_insert((i as i32, i as i32));
                continue;
            }
            let mut val = 0i32;
            for j in i..n.min(i + 30) {
                val = val * 2 + (s[j] - b'0') as i32;
                pos.entry(val).or_insert((i as i32, j as i32));
            }
        }
        queries
            .into_iter()
            .map(|q| {
                let need = q[0] ^ q[1];
                if let Some(&(a, b)) = pos.get(&need) {
                    vec![a, b]
                } else {
                    vec![-1, -1]
                }
            })
            .collect()
    }
}
