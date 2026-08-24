// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

use std::collections::HashMap;

impl Solution {
    pub fn count_palindrome_paths(parent: Vec<i32>, s: String) -> i64 {
        let n = parent.len();
        let mut g = vec![Vec::new(); n];
        for i in 1..n {
            g[parent[i] as usize].push(i);
        }
        let bytes = s.as_bytes();
        let mut freq = HashMap::new();
        freq.insert(0i32, 1i64);
        let mut ans = 0i64;
        fn dfs(
            u: usize,
            mask: i32,
            g: &[Vec<usize>],
            bytes: &[u8],
            freq: &mut HashMap<i32, i64>,
            ans: &mut i64,
        ) {
            for &v in &g[u] {
                let nm = mask ^ (1 << (bytes[v] - b'a'));
                *ans += *freq.get(&nm).unwrap_or(&0);
                for b in 0..26 {
                    *ans += *freq.get(&(nm ^ (1 << b))).unwrap_or(&0);
                }
                *freq.entry(nm).or_insert(0) += 1;
                dfs(v, nm, g, bytes, freq, ans);
            }
        }
        dfs(0, 0, &g, bytes, &mut freq, &mut ans);
        ans
    }
}
