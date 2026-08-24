#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

use std::collections::HashMap;

impl Solution {
    pub fn max_partitions_after_operations(s: String, k: i32) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut memo: HashMap<i64, i32> = HashMap::new();
        fn key(i: usize, cur: i32, t: i32) -> i64 {
            ((i as i64) << 32) | ((cur as i64) << 1) | t as i64
        }
        fn dfs(
            i: usize,
            cur: i32,
            t: i32,
            n: usize,
            b: &[u8],
            k: i32,
            memo: &mut HashMap<i64, i32>,
        ) -> i32 {
            if i >= n {
                return 1;
            }
            let kkey = key(i, cur, t);
            if let Some(&v) = memo.get(&kkey) {
                return v;
            }
            let v = 1 << (b[i] - b'a');
            let nxt = cur | v;
            let mut ans = if nxt.count_ones() as i32 > k {
                dfs(i + 1, v, t, n, b, k, memo) + 1
            } else {
                dfs(i + 1, nxt, t, n, b, k, memo)
            };
            if t > 0 {
                for j in 0..26 {
                    let nxt = cur | (1 << j);
                    if nxt.count_ones() as i32 > k {
                        ans = ans.max(dfs(i + 1, 1 << j, 0, n, b, k, memo) + 1);
                    } else {
                        ans = ans.max(dfs(i + 1, nxt, 0, n, b, k, memo));
                    }
                }
            }
            memo.insert(kkey, ans);
            ans
        }
        dfs(0, 0, 1, n, b, k, &mut memo)
    }
}
